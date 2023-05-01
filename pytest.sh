clear

export PYTHON_VER=$(sed -n -e 's/^python = //p' pyproject.toml)
echo $(echo "$PYTHON_VER" | grep -o -E '[0-9|.]+')
export PYTHON_VER=$(echo "$PYTHON_VER" | grep -o -E '[0-9|.]+')
sed -i "/          python-version:/c\          python-version: '$PYTHON_VER'" ./.github/workflows/pipeline.yaml 

task test
