#!/usr/bin/env sh
# Gera o e-book da documentação: build estático (Docker) + PDF.
# Saída: dist/documentacao-brasil-participativo.pdf
#
# Em Macs com Apple Silicon, a imagem do Puppeteer (só amd64) roda emulada e fica muito lenta;
# nesse caso o PDF é gerado com o Node e o Google Chrome instalados na máquina.
set -e
cd "$(dirname "$0")/.."

DOC_VERSION="$(git rev-parse --short HEAD 2>/dev/null || echo local)"
export DOC_VERSION
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
OUT="dist/documentacao-brasil-participativo.pdf"

docker compose run --rm docs build --strict -d dist/site

if [ "$(uname -m)" = "arm64" ] && command -v node >/dev/null 2>&1 && [ -x "$CHROME" ]; then
  PUPPETEER_SKIP_DOWNLOAD=1 npm install --silent --no-save --prefix .pdf puppeteer@25.12.0 pdf-lib@1.17.1
  NODE_PATH=.pdf/node_modules PUPPETEER_EXECUTABLE_PATH="$CHROME" node scripts/gerar_pdf.cjs dist/site "$OUT"
else
  docker compose --profile pdf run --rm pdf
fi
