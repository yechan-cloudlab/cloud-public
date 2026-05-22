# Keycloak MCP Admin Automation

테스트 Realm에서 Keycloak 관리 작업을 AI 클라이언트로 자동화하는 MCP 서버 샘플입니다.

> ⚠️ 이 프로젝트는 테스트 Realm 전용 샘플입니다. 권한, 감사 로그, 승인 흐름, 속도 제한, 롤백 전략을 검토하지 않고 프로덕션 Realm에 직접 연결하지 마세요.

---

## 📎 관련 아티클

- [Claude한테 "키클락 유저 100명 생성해줘" 했더니 10초 만에 끝났다: Keycloak MCP 자동화 실전](https://tistory-cloud.tistory.com/entry/Claude%ED%95%9C%ED%85%8C-%E2%80%9C%ED%82%A4%ED%81%B4%EB%9D%BD-%EC%9C%A0%EC%A0%80-100%EB%AA%85-%EC%83%9D%EC%84%B1%ED%95%B4%EC%A4%98%E2%80%9D-%ED%96%88%EB%8D%94%EB%8B%88-10%EC%B4%88-%EB%A7%8C%EC%97%90-%EB%81%9D%EB%82%AC%EB%8B%A4-Keycloak-MCP-%EC%9E%90%EB%8F%99%ED%99%94-%EC%8B%A4%EC%A0%84)

이 아티클에서 dry-run, rollback, 서비스 계정 범위, 테스트 Realm 전용 가드레일의 운영 맥락을 설명합니다.

---

## ✅ 이 예제가 보여주는 것

AI 클라이언트(Claude Desktop, Cursor)가 Keycloak을 직접 수정하지 않고, 제한된 MCP 서버를 통해 가드레일을 거쳐 Keycloak Admin REST API를 호출하는 안전한 패턴입니다.

```text
"Create 30 development team users and assign grafana-reader role. Run dry-run first."
```

**제공 기능**

| 기능 | 포함 여부 |
| --- | --- |
| 대량 사용자 생성 | ✅ |
| Realm 역할 할당 | ✅ |
| 사용자 유효성 검사 | ✅ |
| disable/delete 롤백 | ✅ |
| dryRun 기본값 | ✅ |
| Realm 허용 목록 | ✅ |
| 배치 크기 제한 | ✅ |
| 감사 로그 | ✅ |
| 프로덕션용 IAM 플랫폼 | ❌ |

**안전 기본값**

| 항목 | 기본값 |
| --- | --- |
| 쓰기 작업 | 명시적으로 활성화하지 않으면 비활성화 |
| 도구 실행 | `dryRun: true` 우선 |
| Realm 접근 | 허용 목록 필수 |
| 롤백 | `delete`보다 `disable` 권장 |
| 감사 로그 | JSON lines → stderr |
| 프로덕션 Realm | 권장하지 않음 |

**아키텍처**

```text
Claude Desktop / Cursor
        |
        | MCP tool call
        v
Keycloak MCP Admin Automation Server
        |
        | Guardrails + dryRun + audit log
        v
Keycloak Admin REST API
        |
        v
Test Realm
```

**제공 도구**

| 도구 | 목적 | 기본 동작 |
| --- | --- | --- |
| `bulk_user_create` | 다수 Keycloak 사용자 생성 | `dryRun: true` |
| `assign_roles` | 사용자에게 Realm 역할 할당 | `dryRun: true` |
| `validate_users` | 사용자 존재 여부 및 역할 확인 | read-only |
| `rollback_users` | 생성된 사용자 비활성화 또는 삭제 | `dryRun: true`, `disable` 권장 |

---

## 📁 폴더 구조

```text
keycloak-mcp-admin-automation/
|- README.md
|- SECURITY.md
|- .env.example
|- docker-compose.yml
|- src/
|  |- index.ts
|  |- config.ts
|  |- keycloak-client.ts
|  |- audit.ts
|  |- guardrails.ts
|  |- tools/
|     |- bulk-user-create.ts
|     |- assign-roles.ts
|     |- validate-users.ts
|     |- rollback-users.ts
|- examples/
|  |- claude-desktop-mcp.json
|  |- cursor-mcp.json
|  |- users.sample.csv
|  |- users.sample.json
|  |- prompts.md
|- scripts/
|  |- validate-repo.mjs
|  |- smoke-test.mjs
|- docs/
   |- architecture.md
   |- safety-model.md
   |- keycloak-permissions.md
   |- dry-run-and-rollback.md
   |- audit-log.md
   |- production-warning.md
```

---

## 🚀 빠른 시작

**1. 의존성 설치**

```bash
npm install
```

**2. 테스트용 로컬 Keycloak 시작**

```bash
docker compose up -d
```

Keycloak 접속: `http://localhost:8080`  
기본 로컬 관리자 계정 (`docker-compose.yml` 기준): `admin` / `admin`

**3. 테스트 Realm 및 서비스 계정 생성**

`demo` Realm과 `mcp-admin-automation` confidential 클라이언트를 생성합니다.  
참고: `docs/keycloak-permissions.md`, `docs/production-warning.md`

**4. 환경 설정**

```bash
cp .env.example .env
```

`.env`를 테스트 Keycloak 값으로 업데이트합니다.

```env
KEYCLOAK_ALLOWED_REALMS=demo
KEYCLOAK_ALLOW_WRITE_TOOLS=false
KEYCLOAK_DEFAULT_DRY_RUN=true
```

**5. 빌드 및 검증**

```bash
npm run build
npm run validate
```

**6. Claude Desktop 또는 Cursor에서 연결**

- `examples/claude-desktop-mcp.json`
- `examples/cursor-mcp.json`

`/absolute/path/to/keycloak-mcp-admin-automation/dist/index.js`를 로컬 경로로 교체하세요.

**예제 프롬프트**

```text
# 사용자 생성 dry-run
Create 50 marketing team users in the demo realm.
Use usernames marketing001 to marketing050.
Use emails marketing001@example.com to marketing050@example.com.
Set temporary password Temp123!ChangeMe.
Require password update on first login.
Run dry-run first.

# 역할 할당
Assign grafana-reader role to marketing001 through marketing050 in the demo realm.
Run dry-run first.

# 롤백
Disable marketing001 through marketing050 in the demo realm.
Run dry-run first.
```

---

## ⚠️ 사용 전 확인

프로덕션에서 사용하려면 아래 항목을 반드시 검토하세요.

- 별도 서비스 계정 구성
- 최소 Keycloak 관리자 역할 부여
- Realm 허용 목록 설정
- dry-run 승인 단계 추가
- 감사 로그 보존 정책
- 속도 제한 설정
- 롤백 계획 수립
- 변경 승인 워크플로우
- Secret Manager 연동
- 사용자 데이터 처리 정책 검토

---

## 📚 참고 문서

- `docs/architecture.md`
- `docs/safety-model.md`
- `docs/keycloak-permissions.md`
- `docs/dry-run-and-rollback.md`
- `docs/audit-log.md`
- `docs/production-warning.md`

---

## License

MIT
