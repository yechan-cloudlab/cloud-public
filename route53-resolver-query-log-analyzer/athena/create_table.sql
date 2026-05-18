CREATE EXTERNAL TABLE IF NOT EXISTS r53_rlogs (
  version string,
  account_id string,
  region string,
  vpc_id string,
  query_timestamp string,
  query_name string,
  query_type string,
  query_class string,
  rcode string,
  answers array<struct<Rdata:string,Type:string,Class:string>>,
  srcaddr string,
  srcport int,
  transport string,
  srcids struct<instance:string,resolver_endpoint:string>,
  firewall_rule_action string,
  firewall_rule_group_id string,
  firewall_domain_list_id string
)
PARTITIONED BY (
  `date` string,
  `vpc` string
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
STORED AS INPUTFORMAT 'org.apache.hadoop.mapred.TextInputFormat'
OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION 's3://YOUR_BUCKET/route53-query-logging/AWSLogs/YOUR_ACCOUNT_ID/vpcdnsquerylogs/'
TBLPROPERTIES (
  'projection.enabled' = 'true',
  'projection.vpc.type' = 'enum',
  'projection.vpc.values' = 'vpc-xxxxxxxx',
  'projection.date.type' = 'date',
  'projection.date.range' = '2026/01/01,NOW',
  'projection.date.format' = 'yyyy/MM/dd',
  'projection.date.interval' = '1',
  'projection.date.interval.unit' = 'DAYS',
  'storage.location.template' = 's3://YOUR_BUCKET/route53-query-logging/AWSLogs/YOUR_ACCOUNT_ID/vpcdnsquerylogs/${vpc}/${date}/'
);
