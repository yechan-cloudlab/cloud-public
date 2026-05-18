-- Replace the date filters before running in production.

-- 1) 최근 조회량 상위 도메인
SELECT
  query_name,
  COUNT(*) AS query_count,
  COUNT(DISTINCT srcids.instance) AS instance_count
FROM r53_rlogs
WHERE date BETWEEN '2026/05/01' AND '2026/05/18'
GROUP BY query_name
ORDER BY query_count DESC
LIMIT 50;

-- 2) 인스턴스별 조회 도메인
SELECT
  srcids.instance AS instance_id,
  query_name,
  COUNT(*) AS query_count
FROM r53_rlogs
WHERE date = '2026/05/18'
GROUP BY srcids.instance, query_name
ORDER BY query_count DESC;

-- 3) NXDOMAIN 급증 탐지
SELECT
  srcids.instance AS instance_id,
  COUNT(*) AS nxdomain_count
FROM r53_rlogs
WHERE date = '2026/05/18'
  AND rcode = 'NXDOMAIN'
GROUP BY srcids.instance
HAVING COUNT(*) >= 20
ORDER BY nxdomain_count DESC;

-- 4) 긴 도메인 탐지
SELECT
  srcids.instance AS instance_id,
  query_name,
  LENGTH(query_name) AS domain_length,
  COUNT(*) AS query_count
FROM r53_rlogs
WHERE date = '2026/05/18'
  AND LENGTH(query_name) >= 50
GROUP BY srcids.instance, query_name
ORDER BY domain_length DESC, query_count DESC;

-- 5) TXT 쿼리 과다 탐지
SELECT
  srcids.instance AS instance_id,
  query_name,
  COUNT(*) AS txt_query_count
FROM r53_rlogs
WHERE date = '2026/05/18'
  AND query_type = 'TXT'
GROUP BY srcids.instance, query_name
HAVING COUNT(*) >= 10
ORDER BY txt_query_count DESC;

-- 6) Python 리포트 생성기 입력용 집계 쿼리
SELECT
  srcids.instance AS instance_id,
  query_name,
  query_type,
  rcode,
  COUNT(*) AS query_count
FROM r53_rlogs
WHERE date = '2026/05/18'
GROUP BY srcids.instance, query_name, query_type, rcode
ORDER BY query_count DESC;
