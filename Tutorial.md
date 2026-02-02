# Guia Completo: Como Clonar Sua Voz

## 📁 PASSO 1: PREPARAR ÁUDIOS

Coloque seus áudios na pasta:
`/workspaces/RVC-DAVI/datasets/minha_voz/`

Você precisa de:

- 10-30 minutos de gravação da sua voz
- Áudio limpo (sem música, sem eco, sem ruído)
- Formatos: WAV, MP3, FLAC

## 📝 PASSO 2: NA INTERFACE WEB (<http://localhost:7865>)

Vá na aba "Train" e siga:

### 1️⃣ CONFIGURAÇÃO INICIAL

- Experiment Name: minha_voz (ou outro nome)
- Target sample rate: 48k (melhor qualidade)
- Pitch guidance: True (para canto) ou False (para fala)

### 2️⃣ PROCESSAR DADOS

- Em "Enter the path of the training folder"
  Digite: `/workspaces/RVC-DAVI/datasets/minha_voz`
- Clique em "Process Data"
- Aguarde processar todos os áudios

### 3️⃣ EXTRAIR FEATURES

- Pitch extraction: rmvpe (melhor qualidade)
- Clique em "Feature Extraction"
- Aguarde extrair características

### 4️⃣ TREINAR

- Save frequency: 10-25
- Total epochs: 200-500 (mais = melhor, mas mais lento)
- Batch size: 4-8 (em CPU use 4)
- Clique em "Train Model"

### ⏱️ TEMPO ESTIMADO (CPU)

- Processamento: 5-10 min
- Extração: 10-20 min
- Treino: VÁRIAS HORAS (CPU é lento!)

### 5️⃣ USAR O MODELO

- Após treinar, vá na aba "Model Inference"
- Selecione seu modelo "minha_voz"
- Carregue um áudio e converta!

> ⚠️ **DICA:** Para resultados bons, treine pelo menos 200 épocas. Pode deixar rodando durante a noite.
