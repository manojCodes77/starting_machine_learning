# Creating Python Virtual Environments

There are multiple methods to create and manage Python virtual environments:

## 1. Using venv (Built-in)
```bash
# Create virtual environment
python -m venv myenv

# Activate virtual environment
# Windows CMD
myenv\Scripts\activate

# Windows PowerShell
myenv\Scripts\Activate.ps1

# Deactivate
deactivate
```

## 2. Using Conda
```bash
# Create virtual environment
conda create -p venv python==3.12 -y

# Activate
conda activate ${path}\venv

# Deactivate
conda deactivate
```

## 3. setting up the requirements.txt
```bash
# Create requirements.txt
pip install -r requirements.txt
```

## 4. To install a package in the ipynb file itself
```python
!pip install package_name
```
