#!/bin/bash

# Activate conda environment
conda activate phidata

# changes to rag app dir
rag_run="cd C:\Users\user\projects\phidata\cookbook\llms\groq\rag"

# Execute the command
$rag_run

# Run streamlit
streamlit run app.py