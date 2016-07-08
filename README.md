# RBLC (Robocopy Backup Log Check)
Ferramenta para analise de logs do Robocopy
- Faça o dowload do arquivo BRLC.exe
- Abra o cmd e navegue até o local onde esta o BRLC.exe
- Digite BRLC.exe [diretorio dos logs] > arquivo onde o log sera escrito

#Exemplo de execução
BRLC.exe C:\Users\matheus\Desktop\backup\logs\01-Segunda > saida.txt

#Exemplo de saída:
logs\01-Segunda 
...Administrativo.TXT 
...Data Inicio:04/07/16
...Erros:0
...Data Fim:04/07/16
logs\01-Terça 
...Administrativo.TXT 
...Data Inicio:05/07/16
...Erros:30
...Data Fim:05/07/16

#Erro Conhecido
"O programa não pode ser iniciado porque está faltando msvrc100.dll no seu computador..."
Para corrigir este erro instale o seguinte software
Windows x86
https://www.microsoft.com/en-us/download/details.a...
Windows x64
https://www.microsoft.com/en-us/download/details.aspx?id=14632
