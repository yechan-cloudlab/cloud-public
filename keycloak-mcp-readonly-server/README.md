# Keycloak MCP Readonly Server

AI Agent로 Keycloak 설정을 조회하는 읽기 전용 MCP 서버 샘플입니다.

> 이 저장소는 블로그 시리즈를 위한 **학습용 샘플**입니다. 공식 Keycloak 또는 MCP 프로젝트가 아니며, 기본 설계는 의도적으로 읽기 전용입니다.

---

## 📎 관련 아티클

- [Part 1: Keycloak MCP란 무엇인가: AI Agent로 인증 설정을 점검하는 읽기 전용 서버 만들기](https://tistory-cloud.tistory.com/entry/Keycloak-MCP%EB%9E%80-%EB%AC%B4%EC%97%87%EC%9D%B8%EA%B0%80-AI-Agent%EB%A1%9C-%EC%9D%B8%EC%A6%9D-%EC%84%A4%EC%A0%95%EC%9D%84-%EC%A0%90%EA%B2%80%ED%95%98%EB%8A%94-%EC%9D%BD%EA%B8%B0-%EC%A0%84%EC%9A%A9-%EC%84%9C%EB%B2%84-%EB%A7%8C%EB%93%A4%EA%B8%B0)
- [Part 2: Keycloak MCP 서버 만들기: Realm, Client, User 조회 Tool을 TypeScript로 구현하기](https://tistory-cloud.tistory.com/entry/Keycloak-MCP-%EC%84%9C%EB%B2%84-%EB%A7%8C%EB%93%A4%EA%B8%B0-Realm-Client-User-%EC%A1%B0%ED%9A%8C-Tool%EC%9D%84-TypeScript%EB%A1%9C-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0)
- [Part 3: Keycloak MCP 보안 운영 가이드: AI Agent에게 인증 시스템을 어디까지 보여줄 것인가](https://tistory-cloud.tistory.com/entry/Keycloak-MCP-%EB%B3%B4%EC%95%88-%EC%9A%B4%EC%98%81-%EA%B0%80%EC%9D%B4%EB%93%9C-AI-Agent%EC%97%90%EA%B2%8C-%EC%9D%B8%EC%A6%9D-%EC%8B%9C%EC%8A%A4%ED%85%9C%EC%9D%84-%EC%96%B4%EB%94%94%EA%B9%8C%EC%A7%80-%EB%B3%B4%EC%97%AC%EC%A4%84-%EA%B2%83%EC%9D%B8%EA%B0%80)

---

## ✅ 이 예제가 보여주는 것

- Keycloak Admin API를 좁은 범위의 MCP 도구로 래핑하는 방법
- AI Agent에게 읽기 전용 조회 도구를 노출하는 방법
- Realm, Client, Redirect URI, 사용자, 관리자 역할 확인 방법
- 위험한 쓰기 작업을 MCP 서버에서 제외하는 방법
- 프로덕션 Keycloak 연결 전 보안 가드레일 문서화

## ❌ 이 예제가 하지 않는 것

- Keycloak 리소스를 생성, 수정, 삭제하지 않습니다.
- Client Secret을 반환하지 않습니다.
- 사용자 비밀번호를 초기화하지 않습니다.
- 프로덕션 수준의 인증, 권한, 감사, 네트워크 제어를 포함하지 않습니다.
- 인증 시스템 변경에 대한 사람의 검토를 대신하지 않습니다.

**아키텍처**

```text
AI Client / MCP Host
  |
  | MCP stdio tool call
  v
Keycloak MCP Readonly Server
  |
  | OAuth2 Client Credentials
  v
Keycloak Admin API
```

MCP 서버가 안전 경계입니다. Keycloak Admin API를 AI Agent에 직접 노출하지 마세요.

**제공 도구**

| 도구 | 목적 | 비고 |
|---|---|---|
| `list_realms` | 서비스 계정에 보이는 Realm 목록 조회 | 제한된 서비스 계정에서만 사용 |
| `list_clients` | Realm의 Client 목록 조회 | Client Secret 반환 안 함 |
| `check_redirect_uris` | 위험한 Redirect URI 패턴 탐지 | 와일드카드, localhost 패턴 플래그 |
| `list_users` | 제한된 사용자 메타데이터 조회 | 이메일 값 마스킹 |
| `check_admin_roles` | 관리자 유사 Realm 역할 목록 조회 | 전체 할당 조회 미지원 |

---

## 📁 폴더 구조

```text
src/                 MCP 서버 및 Keycloak 클라이언트 코드
src/tools/           읽기 전용 MCP 도구 구현
docs/                아키텍처, 도구 설계, 보안 모델, 운영 체크리스트
examples/            MCP 클라이언트 설정 및 샘플 프롬프트
scripts/             저장소 검증 스크립트
.env.example         로컬 환경 변수 템플릿
```

---

## 🚀 빠른 시작

```bash
npm install
cp .env.example .env
npm run build
npm start
```

Windows PowerShell:

```powershell
Copy-Item .env.example .env
npm install
npm run build
npm start
```

`.env` 파일을 편집한 후 실행하세요.

**환경 변수**

```env
KEYCLOAK_BASE_URL=https://keycloak.example.com
KEYCLOAK_ADMIN_REALM=master
KEYCLOAK_TARGET_REALM=sample
KEYCLOAK_CLIENT_ID=mcp-readonly
KEYCLOAK_CLIENT_SECRET=replace-me
KEYCLOAK_ALLOW_WRITE_TOOLS=false
```

MCP 클라이언트 설정은 `examples/claude-desktop-config.json`을 참고하세요.

---

## ⚠️ 사용 전 확인

- Node.js 20 이상이 필요합니다.
- 전용 Keycloak 서비스 계정을 사용하세요.
- 조회에 필요한 최소 realm-management 역할만 부여하세요.
- 이 MCP 서버를 공개 인터넷에 직접 노출하지 마세요.
- 개발 Realm 테스트 완료 전에 프로덕션 Realm을 연결하지 마세요.
- 도구 호출, 대상 Realm, 호출자 컨텍스트를 로깅하세요.

**검증 명령**

```bash
npm run validate   # 저장소 정적 검사
npm run typecheck  # 타입 체크
npm run build      # 빌드
```

---

## 📚 참고 문서

- [Model Context Protocol TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Model Context Protocol documentation](https://modelcontextprotocol.io/)
- [Keycloak Server Administration Guide](https://www.keycloak.org/docs/latest/server_admin/)
- [Keycloak Admin REST API](https://www.keycloak.org/docs-api/latest/rest-api/)

---

## License

MIT License. See `LICENSE`.
