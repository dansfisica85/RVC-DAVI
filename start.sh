#!/bin/bash
# Script para iniciar o Applio-RVC-Fork (versão CPU)

# Diretório do projeto
cd /workspaces/RVC-DAVI

# Ativar ambiente virtual
source venv/bin/activate

# Verificar se os modelos necessários existem
if [ ! -f "hubert_base.pt" ]; then
    echo "Baixando hubert_base.pt..."
    curl -# -L -o "hubert_base.pt" "https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/hubert_base.pt"
fi

if [ ! -f "rmvpe.pt" ]; then
    echo "Baixando rmvpe.pt..."
    curl -# -L -o "rmvpe.pt" "https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/rmvpe.pt"
fi

# Criar diretórios necessários
mkdir -p logs audios datasets weights audio-outputs audio-others TEMP

# Definir variáveis de ambiente para CPU
export PYTORCH_ENABLE_MPS_FALLBACK=0
export CUDA_VISIBLE_DEVICES=""
export TF_CPP_MIN_LOG_LEVEL=3
export OPENBLAS_NUM_THREADS=1

# Iniciar a aplicação
echo "Iniciando Applio-RVC-Fork..."
echo "Acesse: http://localhost:7865"
echo ""
python infer-web.py --pycmd python
