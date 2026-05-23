import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();

const requiredFiles = [
  'README.md',
  'LICENSE',
  'charts-values/istio-base-values.yaml',
  'charts-values/istiod-values.yaml',
  'charts-values/istio-gateway-values.yaml',
  'install/01-add-helm-repo.sh',
  'install/02-install-base.sh',
  'install/03-install-istiod.sh',
  'install/04-install-gateway.sh',
  'install/05-verify.sh',
  'sample-app/namespace.yaml',
  'sample-app/serviceaccount-frontend.yaml',
  'sample-app/frontend.yaml',
  'sample-app/app-v1.yaml',
  'sample-app/app-v2.yaml',
  'sample-app/service.yaml',
  'traffic-routing/gateway.yaml',
  'traffic-routing/destinationrule.yaml',
  'traffic-routing/virtualservice-canary.yaml',
  'traffic-routing/virtualservice-header.yaml',
  'mtls-security/peerauthentication-strict.yaml',
  'mtls-security/authorizationpolicy-allow-only-frontend.yaml',
  'mtls-security/destinationrule-mtls.yaml',
  'troubleshooting/commands-cheatsheet.md',
];

const requiredReadmeSnippets = [
  'Istio install with Helm',
  'Istio란 무엇인가',
  'Istio Helm Chart 설치 방법',
  'Istio Canary 배포 방법',
  'Istio mTLS 설정 방법',
  'Istio 관측성 운영 방법',
  'Istio 트러블슈팅 가이드',
];

const yamlFiles = requiredFiles.filter((file) => file.endsWith('.yaml'));

const errors = [];

for (const file of requiredFiles) {
  if (!fs.existsSync(path.join(root, file))) {
    errors.push(`Missing required file: ${file}`);
  }
}

const readme = fs.readFileSync(path.join(root, 'README.md'), 'utf8');
for (const snippet of requiredReadmeSnippets) {
  if (!readme.includes(snippet)) {
    errors.push(`README missing snippet: ${snippet}`);
  }
}

for (const file of yamlFiles) {
  const content = fs.readFileSync(path.join(root, file), 'utf8');
  if (!content.includes('apiVersion:') || !content.includes('kind:')) {
    if (!file.startsWith('charts-values/') && !file.startsWith('observability/')) {
      errors.push(`YAML file may be missing apiVersion/kind: ${file}`);
    }
  }
}

const gateway = fs.readFileSync(path.join(root, 'traffic-routing/gateway.yaml'), 'utf8');
if (!gateway.includes('selector:') || !gateway.includes('istio: ingress')) {
  errors.push('Gateway selector should be reviewed. Expected selector label istio: ingress for this sample.');
}

if (errors.length > 0) {
  console.error(errors.join('\n'));
  process.exit(1);
}

console.log('Repository validation passed.');
