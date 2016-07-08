# RBLC (Robocopy Backup Log Check)
Ferramenta para analise de logs do Robocopy
- Faça o dowload do arquivo BRLC.exe
- Abra o cmd e navegue até o local onde esta o BRLC.exe
- Digite BRLC.exe [diretorio dos logs] > arquivo onde o log sera escrito

#Exemplo de execução
BRLC.exe C:\Users\matheus\Desktop\backup\logs\01-Segunda > saida.txt

#Exemplo de saída
<pre>logs\01-Segunda 
...Administrativo.TXT 
...Data Inicio:04/07/16
...Erros:0
...Data Fim:04/07/16
logs\01-Terça 
...Administrativo.TXT 
...Data Inicio:05/07/16
...Erros:30
...Data Fim:05/07/16
</pre>

#Erro Conhecido
<pre>
"O programa não pode ser iniciado porque está faltando msvrc100.dll no seu computador..."
Para corrigir este erro instale o seguinte software

#Compilar no Windows
<pre>
- Instale o python 2.7
- Instale a lib pyinstaller através do cmd executando o seguinte comando
pip install pyinstaller
- Execute o seguinte comando através do cmd para compilar o source
pyinstaller --onefile RBLC.py 
</pre>
O arquivo compilado será salvo dentro da pasta dist.


Windows x86
https://www.microsoft.com/en-us/download/details.aspx?id=5555

Windows x64
https://www.microsoft.com/en-us/download/details.aspx?id=14632
</pre>
