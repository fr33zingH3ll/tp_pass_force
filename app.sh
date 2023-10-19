#!/bin/bash

# Variables
os_info=$(uname)
venv="tp_pass_force_venv"
module_name="index"
destination="html/tp_pass_force"

# Vérifiez le système d'exploitation
if [ "$os_info" == "Linux" ]; then
    echo "Système d'exploitation : Linux"
    source "$venv"/bin/activate
elif [ "$os_info" == "Darwin" ]; then
    echo "Système d'exploitation : macOS"
    source "$venv"/bin/activate
elif [ "$os_info" == "MINGW64_NT-10.0-19045" ]; then  # Vérifiez la chaîne de la fenêtre Git Bash pour Windows
    echo "Système d'exploitation : Windows"
    source "./$venv\Scripts\activate"
else
    echo "Système d'exploitation non reconnu : $os_info"
fi

# Mettre a jour pip
pip install --upgrade pip

# Installez les dépendances à partir du fichier requirements.txt
pip install -r requirements.txt

# Générez la documentation HTML avec pdoc
pdoc --html .

# Ouvrez la documentation générée en fonction de la plateforme
if [ "$os_info" == "Linux" ]; then
    xdg-open "$destination/$module_name.html"  # Pour les systèmes Linux
elif [ "$os_info" == "Darwin" ]; then
    open "$destination/$module_name.html"  # Pour les systèmes macOS
elif [ "$os_info" == "MINGW64_NT-10.0-19045" ]; then
    start "$destination\\$module_name.html"  # Pour les systèmes Windows (Git Bash)
else
    echo "L'ouverture de la documentation n'est pas prise en charge sur ce système."
fi
