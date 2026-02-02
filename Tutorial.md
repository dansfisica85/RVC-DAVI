# 🎤 RVC-DAVI: Guia Completo de Clonagem de Voz

Clone sua voz usando inteligência artificial com o RVC (Retrieval-based Voice Conversion).

---

## 🚀 Início Rápido

### Iniciar a Interface Web

```bash
# Ativar ambiente virtual
source /workspaces/RVC-DAVI/venv/bin/activate

# Iniciar o servidor
python infer-web.py
```

Acesse: **<http://localhost:7865>**

---

## 📁 PASSO 1: Preparar Áudios de Treino

### Criar pasta do dataset

```bash
mkdir -p /workspaces/RVC-DAVI/datasets/minha_voz
```

### Coloque seus áudios na pasta

`/workspaces/RVC-DAVI/datasets/minha_voz/`

### Requisitos dos áudios

| Requisito | Recomendação |
|-----------|--------------|
| **Duração total** | 10-30 minutos |
| **Qualidade** | Áudio limpo, sem ruído/eco |
| **Formatos** | WAV, MP3, FLAC |
| **Conteúdo** | Apenas sua voz falando/cantando |

> 💡 **Dica:** Quanto mais variado o conteúdo (diferentes tons, emoções), melhor o modelo!

---

## 📝 PASSO 2: Treinar o Modelo

Acesse a interface web em **<http://localhost:7865>** e vá na aba **"Train"**.

### 1️⃣ Configuração Inicial

| Campo | Valor Recomendado |
|-------|-------------------|
| **Experiment Name** | `minha_voz` (ou outro nome) |
| **Target sample rate** | `48k` (melhor qualidade) |
| **Pitch guidance** | `True` (canto) ou `False` (fala) |

### 2️⃣ Processar Dados

1. Em **"Enter the path of the training folder"**, digite:
   ```
   /workspaces/RVC-DAVI/datasets/minha_voz
   ```
2. Clique em **"Process Data"**
3. Aguarde o processamento (5-10 min)

### 3️⃣ Extrair Features

1. **Pitch extraction algorithm:** `rmvpe` (melhor qualidade)
2. Clique em **"Feature Extraction"**
3. Aguarde a extração (10-20 min)

### 4️⃣ Treinar Modelo

| Parâmetro | Valor Recomendado |
|-----------|-------------------|
| **Save frequency** | 10-25 |
| **Total epochs** | 200-500 |
| **Batch size** | 4 (CPU) ou 8 (GPU) |

Clique em **"Train Model"** e aguarde.

### ⏱️ Tempo Estimado

| Etapa | CPU | GPU |
|-------|-----|-----|
| Processamento | 5-10 min | 2-5 min |
| Extração | 10-20 min | 5-10 min |
| Treino (200 épocas) | 4-8 horas | 30-60 min |

---

## 🎵 PASSO 3: Usar o Modelo

### Na aba "Model Inference"

1. **Selecione seu modelo** em "Inferencing voice"
2. **Carregue um áudio** para converter
3. Ajuste os parâmetros:
   - **Transpose:** Ajusta o tom (-12 a +12 semitons)
   - **Index Rate:** 0.0-1.0 (quanto usa do índice treinado)
4. Clique em **"Convert"**

### Parâmetros Avançados

| Parâmetro | Descrição | Valor Padrão |
|-----------|-----------|--------------|
| **Pitch algorithm** | Algoritmo de extração | `rmvpe` |
| **Index rate** | Similaridade com treino | `0.75` |
| **Filter radius** | Suavização | `3` |
| **Resample** | Taxa de reamostragem | `0` (auto) |
| **Volume envelope** | Mix do volume | `0.25` |
| **Protect voiceless** | Protege consoantes | `0.33` |

---

## 📂 Estrutura de Pastas

```
/workspaces/RVC-DAVI/
├── datasets/           # Seus áudios de treino
│   └── minha_voz/
├── logs/               # Logs e índices do treino
├── weights/            # Modelos treinados (.pth)
├── audio-outputs/      # Áudios convertidos
└── audios/             # Áudios para conversão
```

---

## ❓ Solução de Problemas

### Erro "CUDA out of memory"

- Reduza o **batch size** para 2 ou 4
- Use CPU se não tiver GPU compatível

### Modelo com qualidade ruim

- Aumente o número de **épocas** (mínimo 200)
- Use áudios mais limpos e variados
- Verifique se tem pelo menos 10 min de áudio

### Interface não abre

```bash
# Verifique se o servidor está rodando
ps aux | grep python

# Reinicie o servidor
pkill -f infer-web.py
python infer-web.py
```

---

## 🔗 Links Úteis

- **Projeto Original:** [RVC-Project](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI)
- **Fork Applio:** [Applio-RVC-Fork](https://github.com/SayanoAI/Applio-RVC-Fork)

---

> ⚠️ **IMPORTANTE:** Use esta tecnologia de forma responsável e ética. Não clone vozes de outras pessoas sem permissão.
