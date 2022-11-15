import os
os.system('ECHO instalando todos os seus programas da lista.')
os.system('winget install -e --id Google.Chrome')
os.system('winget install -e --id VideoLAN.VLC')
os.system('winget install -e --id Microsoft.VisualStudioCode')
os.system('winget install -e --id Python.Python.3.9')
os.system('winget install -e --id RARLab.WinRAR')
#avast v
os.system('winget install -e --id XPDNZJFNCR1B07')
os.system('winget install -e --id Discord.Discord')
os.system('ECHO instalando todas as atualizações dos seus programas.')
os.system('winget upgrade --all')
os.system('pause')
os.system('ECHO Todas as atualizações dos seus programas foram instaladas.')
