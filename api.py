from flask import Flask, jsonify, request, redirect
from waitress import serve
import requests
import json
import time

# Initialize a Flask app
app = Flask(__name__)

# Função para registrar atividades no arquivo de log
def log_activity(ip, endpoint):
    print(f'IP: {ip} acessou: {endpoint}')

# parametro obrigatorio. Aviso

with open('users.json', 'r') as json_file:
    user_data = json.load(json_file)

with open('tokens.json', 'r') as json_file:
     tokens = json.load(json_file)

# Abre um arquivo para leitura (modo 'r' para ler)
with open('zika.txt', 'r') as arquivo:
    zika = arquivo.read()

@app.route('/', methods=['GET', 'POST'])
def check_pa():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
        if user == "admin7k" and password == "7kk":
          return '''
<html>
<head>
    <title>Consulta - Center</title>
</head>
<body style="background-color: black; text-align: center;">
    <div style="text-align: center; margin-top: 50px;">
        <img src="https://telegra.ph/file/d3a0efa010bcdd3c6cf0f.jpg" alt="P A 1 n 3 L. AdM" style="border-radius: 50%; width: 100px; height: 100px;">
        <p style="font-size: 24px; font-weight: bold; color: white;">P A 1 n 3 L - Users.</p>

        <select id="consulta-select" style="font-size: 18px; background-color: gray; color: white; border: 2px solid red; border-radius: 20px; padding: 10px; margin-bottom: 10px;" onchange="toggleTokenField()">
            <option value="add_user" style="background-color: gray;">ADD - user. ✅</option>
            <option value="delete_user" style="background-color: gray;">REVOKE - user. ❌</option>
            <option value="add_token" style="background-color: gray;">ADD - token. ✅</option>
            <option value="delete_token" style="background-color: gray;">REVOKE - token. ❌</option>
        </select>

        <div id="user-pass-fields">
            <input type="text" id="consulta-user" placeholder="Usuário..." style="font-size: 18px; width: 300px; background-color: gray; border: 2px solid red; border-radius: 20px; padding: 5px; margin-bottom: 10px;">
            <input type="password" id="consulta-query" placeholder="Senha..." style="font-size: 18px; width: 300px; background-color: gray; border: 2px solid red; border-radius: 20px; padding: 5px; margin-bottom: 10px;">
        </div>

        <div id="token-field" style="display: none;">
            <input type="text" id="consulta-token" placeholder="Token..." style="font-size: 18px; width: 300px; background-color: gray; border: 2px solid red; border-radius: 20px; padding: 5px; margin-bottom: 10px;">
        </div>

        <button onclick="executarConsulta()" style="font-size: 18px; width: 150px; height: 40px; background-color: transparent; color: white; border: 2px solid white; border-radius: 20px; cursor: pointer;">E X E C U T E</button>

        <div id="resultado" style="font-size: 16px; font-family: monospace; font-weight: bold; color: white; margin-top: 20px; background-color: black; padding: 10px; border-radius: 5px;"></div>
        <div id="logins" style="font-size: 16px; font-family: monospace; font-weight: bold; color: white; margin-top: 20px; background-color: black; padding: 10px; border-radius: 5px;"></div>
    </div>

    <script>
    function toggleTokenField() {
        var select = document.getElementById("consulta-select");
        var tokenField = document.getElementById("token-field");
        var userPassFields = document.getElementById("user-pass-fields");

        if (select.value === "add_token" || select.value === "delete_token") {
            tokenField.style.display = "block";
            userPassFields.style.display = "none";
        } else {
            tokenField.style.display = "none";
            userPassFields.style.display = "block";
        }
    }
     function atualizarLogins() {
            fetch("https://consult-center.thznx.repl.co/users.json")
                .then(response => response.text())
                .then(data => {
                    // Formata a lista de logins em uma string
                document.getElementById("logins").innerText = data;
                })
                .catch(error => {
                    document.getElementById("logins").innerText = "Erro ao carregar os logins.";
                });
        }

        // Chama a função para carregar os logins quando a página carregar
        atualizarLogins();

    function executarConsulta() {
        var select = document.getElementById("consulta-select");
        var selectedValue = select.value; // Alterado para obter o valor diretamente

        var user = document.getElementById("consulta-user").value;
        var pass = document.getElementById("consulta-query").value;
        var token = document.getElementById("consulta-token").value;
        
        // Certifique-se de substituir os caracteres indesejados no token e no query, se necessário
        user = encodeURIComponent(user);
        pass = encodeURIComponent(pass);
        token = encodeURIComponent(token);

        var url;

        if (selectedValue === "add_token" || selectedValue === "delete_token") {
            url = `https://consult-center.thznx.repl.co/control-users?type=${selectedValue}&token=${token}`;
        } else {
            url = `https://consult-center.thznx.repl.co/control-users?type=${selectedValue}&user=${user}&pass=${pass}`;
        }

        // Exibe "Aguarde..." enquanto a consulta está em andamento
        document.getElementById("resultado").innerText = "Aguarde...";

        // Realiza a solicitação à API
        fetch(url)
            .then(response => response.text())
            .then(data => {
                // Exibe a resposta da API
                document.getElementById("resultado").innerText = data;
            })
            .catch(error => {
                // Em caso de erro, exibe uma mensagem de erro
                document.getElementById("resultado").innerText = "Erro ao consultar a API.";
            });
    }
    </script>
</body>
</html>
 '''
        if user in user_data and user_data[user] == password:
            apis = "APIS: \n"
            claro = '<a href="https://consult-center.thznx.repl.co/claro" style="color: blue;">Claro.py</a>'
            tel1 = '<a href="https://consult-center.thznx.repl.co/telefonev1?token=SeuToken&query=32999211651" style="color: blue;">TelV1.py</a>'
            nome1 = '<a href="https://consult-center.thznx.repl.co/nomev1?token=SeuToken&query=Jair Messias Bolsonaro" style="color: blue;">Nomev1.py</a>'
            cpf1 = '<a href="https://consult-center.thznx.repl.co/cpfv1?token=SeuToken&query=04655919655" style="color: blue;">CPFv1.py</a>'
            cpf2 = '<a href="https://consult-center.thznx.repl.co/cpfv2?token=SeuToken&query=04655919655" style="color: blue;">CPFv2.py</a>'
            cpf3 = '<a href="https://consult-center.thznx.repl.co/cpfv3?token=SeuToken&query=04655919655" style="color: blue;">CPFv3.py</a>'
            rg1 = '<a href="https://consult-center.thznx.repl.co/rgv1?token=SeuToken&query=69640597" style="color: blue;">RGv1.py</a>'
            return '''
                <html>
                <head>
                    <title>Consulta - Center</title>
                </head>
                <body style="background-color: black; text-align: center;">
                    <div style='text-align: center; margin-top: 50px;'>
                        <img src="https://telegra.ph/file/10570d10912b23cde7612.jpg" alt="Consulta - Center" style="border-radius: 50%; width: 100px; height: 100px;">
                        <p style="font-size: 24px; font-weight: bold; color: white;">C O N S U L T A - center.</p>
                        
                        <select id="consulta-select" style="font-size: 18px; background-color: #E6E6FA; color: white; border: none; border-radius: 20px; padding: 10px; margin-bottom: 10px;">
                            <option value="https://consult-center.thznx.repl.co/cpfv1">CPF - V1 ( Serasa ) 🔍</option>
                            <option value="https://consult-center.thznx.repl.co/cpfv2">CPF - V2 ( Owndata ) 🔍</option>
                            <option value="https://consult-center.thznx.repl.co/cpfv3">CPF - V3 ( Dataprime ) 🔍</option>
                            <option value="https://consult-center.thznx.repl.co/cpfv4">CPF - V4 ( Cadsus ) 🔍</option>
                            <option value="https://consult-center.thznx.repl.co/nomev1">NOME - V1 👥 ( Receita )</option>
                            <option value="https://consult-center.thznx.repl.co/nomev2">NOME - V2 👥 ( Dataprime )</option>
                            <option value="https://consult-center.thznx.repl.co/telv1">📞 TEL - V1 ( Serasa )</option>
                            <option value="https://consult-center.thznx.repl.co/telv2">📞 TEL - V2 ( ProBusca )</option>
                        </select>
                        
                        <input type="password" id="consulta-token" placeholder="SeuToken..." style='font-size: 18px; width: 300px; background-color: #E6E6FA; border: 2px solid #9370DB; border-radius: 20px; padding: 5px; margin-bottom: 10px;'>
                        <button id="toggle-token" style='font-size: 14px; background-color: transparent; color: white; border: none; cursor: pointer;'>Mostrar.</button><br>
                        <input type="text" id="consulta-query" placeholder="Digite sua consulta..." style='font-size: 18px; width: 300px; background-color: #E6E6FA; border: 2px solid #9370DB; border-radius: 20px; padding: 5px; margin-bottom: 10px;'><br>
                        <button onclick="executarConsulta()" style='font-size: 18px; width: 150px; height: 40px; background-color: transparent; color: white; border: none; border-radius: 20px; cursor: pointer;'>A C E S S A R </button><br>
                        <div id="resultado" style="font-size: 16px; font-family: monospace; font-weight: bold; color: white; margin-top: 20px; background-color: black; padding: 10px; border-radius: 5px;"></div>
                    </div>
                    <script>
                        var tokenHidden = true;
                        
                        document.getElementById("toggle-token").addEventListener("click", function() {
                            var tokenInput = document.getElementById("consulta-token");
                            if (tokenHidden) {
                                tokenInput.type = "text";
                                tokenHidden = false;
                                this.textContent = "Ocultar.";
                            } else {
                                tokenInput.type = "password";
                                tokenHidden = true;
                                this.textContent = "Mostrar.";
                            }
                        });

                        function executarConsulta() {
                            var select = document.getElementById("consulta-select");
                            var selectedOption = select.options[select.selectedIndex];
                            var selectedURL = selectedOption.value;
                            var token = document.getElementById("consulta-token").value;
                            var query = document.getElementById("consulta-query").value;

                            // Certifique-se de substituir os caracteres indesejados no token e no query, se necessário
                            token = encodeURIComponent(token);
                            query = encodeURIComponent(query);

                            var url = selectedURL + "?token=" + token + "&query=" + query;

                            // Exibe "Aguarde..." enquanto a consulta está em andamento
                            document.getElementById("resultado").innerText = "Aguarde...";

                            // Realiza a solicitação à API
                            fetch(url)
                                .then(response => response.text())
                                .then(data => {
                                    // Exibe a resposta da API
                                    document.getElementById("resultado").innerText = data;
                                })
                                .catch(error => {
                                    // Em caso de erro, exibe uma mensagem de erro
                                    document.getElementById("resultado").innerText = "Erro ao consultar a API.";
                                });
                        }
                    </script>
                </body>
                </html>
            '''
        else:
            return jsonify({'message': 'Usuário ou senha incorretos. Tente novamente.'})

    return '''
        <html>
        <head>
            <title>Login</title>
        </head>
        <body style="background-color: black; text-align: center;">
            <div style='text-align: center; margin-top: 100px;'>
                <form method="POST">
                    <div style="background-color: black; padding: 10px; display: inline-block;">
                        <input type="text" id="user" name="user" placeholder="Usuário" style='font-size: 18px; width: 300px; background-color: gray; border: 2px solid red; border-radius: 20px; padding: 5px; margin-bottom: 10px;'><br>
                        <input type="password" id="password" name="password" placeholder="Senha" style='font-size: 18px; width: 300px; background-color: gray; border: 2px solid red; border-radius: 20px; padding: 5px; margin-bottom: 10px;'><br>
                        <input type="submit" value="LOGIN" style='font-size: 18px; width: 100px; height: 40px; background-color: red; color: white; border: none; border-radius: 20px; cursor: pointer;'>
                    </div>
                </form>
            </div>
        </body>
        </html>
    '''
    user_ip = request.remote_addr
    log_activity(user_ip, '/')
# checar segundo parametro.
@app.route('/users.json', methods=['GET'])
def usersu():
        user_password_pairs = []

        # Itera pelos dados do arquivo JSON
        for user, password in user_data.items():
            formatted_pair = f"User: {user} | Pass: {password}"
            user_password_pairs.append(formatted_pair)

        # Retorna a lista completa
        return "\n".join(user_password_pairs)


@app.route('/control-users', methods=['GET'])
def control_users():
    user_type = request.args.get('type')
    user = request.args.get('user')
    password = request.args.get('pass')
    token = request.args.get('token')

    if user_type == "add_user":
        if user and password:
            if user not in user_data:
                user_data[user] = password

                with open('users.json', 'w') as json_file:
                    json.dump(user_data, json_file, indent=4)

                return "Login Adicionado! ✅"
            else:
                return "Usuário já existe. Insira outro usuário! ❌"
        else:
            return "Falha ao adicionar usuário. Certifique-se de fornecer um nome de usuário e senha."

    elif user_type == "delete_user":
        if user in user_data and user_data[user] == password:
            del user_data[user]

            with open('users.json', 'w') as json_file:
                json.dump(user_data, json_file, indent=4)

            return "Login Excluído! ✅"
        else:
            return "Usuário não encontrado ou senha incorreta."

    elif user_type == "add_token":
        if token:
            if token not in tokens:
                tokens.append(token)
                with open('tokens.json', 'w') as tokens_file:
                    json.dump(tokens, tokens_file)
                return "Token Adicionado! ✅"
            else:
                return "Token já existe. Insira outro token! ❌"
        else:
            return "Falha ao adicionar token. Certifique-se de fornecer um token."

    elif user_type == "del_token":
        if token:
            if token in tokens:
                tokens.remove(token)
                with open('tokens.json', 'w') as tokens_file:
                    json.dump(tokens, tokens_file)
                return "Token Removido! ✅"
            else:
                return "Token não encontrado! ❌"
        else:
            return "Falha ao remover token. Certifique-se de fornecer um token."

    else:
        return "Tipo de operação inválido. Use 'add' para adicionar usuário e senha, 'delete' para excluir usuário, 'addtoken' para adicionar um token ou 'deltoken' para remover um token."


@app.route('/telv1')
def tel():
    user_ip = request.remote_addr
    log_activity(user_ip, '/tel1')
    
    # Obtenha o token da query string
    token = request.args.get('token')
    
    if token is not None:
        # Verifique se o token existe no JSON de tokens
        if token in tokens:
            query = request.args.get('query')
            if query is not None:
                re = requests.get(f'http://nexus.vortexuscloud.com:4144/tel?query={query}&token=EuSouPika')
                rr = re.json()
                msg = rr.get('msg')
                if msg == "telefone não encontrado":
                  return "Nao encontrado."
                res = rr.get('resultado')
                nome = res.get('Nome')
                cpf = res.get('Cpf_cnpj')
                end = res.get('endereco')
                num = res.get('numero')
                bar = res.get('bairro')
                city = res.get('cidade')
                cep = res.get("cep")
                if res is not None:
                    return f"📞 CONSULTA TELEFONE SERASA 📞\n\nNOME: {nome}\nCPF: {cpf}\nENDERECO: {end}\nNUMERO: {num}\nBAIRRO: {bar}\nCIDADE: {city}\nCEP: {cep}"
                else:
                    response = {
                        "erro": "Não foi possível obter o resultado.",
                        "status": "404"
                    }
            else:
                response = {
                    "erro": "Parâmetro ?query= não foi fornecido na URL.",
                    "status": "404"
                }
        else:
            response = {
                "erro": "Token inválido.",
                "status": "401"
            }
    else:
        response = {
            "erro": "Token não fornecido na URL. Por favor, inclua um token válido.",
            "status": "401"
        }
    
    return jsonify(response)

@app.route('/telv2')
def tel2():
    user_ip = request.remote_addr
    log_activity(user_ip, '/tel2')
    
    # Obtenha o token da query string
    token = request.args.get('token')
    
    if token is not None:
        # Verifique se o token existe no JSON de tokens
        if token in tokens:
            query = request.args.get('query')
            if query is not None:
                re = requests.get(f'http://nexus.vortexuscloud.com:4144/tel2?query={query}&token=EuSouPika')
                rr = re.json()
                msg = rr.get('msg')
                if msg == "telefone não encontrado":
                  return "Nao encontrado."
                res = rr.get('resultado')
                nome = res.get('nome')
                cpf = res.get('cpf_cnpj')
                log = res.get('logradouro')
                num = res.get('numero')
                bar = res.get('bairro')
                city = res.get('cidade')
                cep = res.get('cep')
                est = res.get('estado')
                if res is not None:
                  return f"📞 CONSULTA TELEFONE PROBUSCA 📞\n\nNOME: {nome}\nCPF: {cpf}\nLOGRADOURO: {log}\nNUMERO: {num}\nBAIRRO: {bar}\nCIDADE: {city}\nCEP: {cep}\nESTADO: {est}"
                else:
                    response = {
                        "erro": "Não foi possível obter o resultado.",
                        "status": "404"
                    }
            else:
                response = {
                    "erro": "Parâmetro ?query= não foi fornecido na URL.",
                    "status": "404"
                }
        else:
            response = {
                "erro": "Token inválido.",
                "status": "401"
            }
    else:
        response = {
            "erro": "Token não fornecido na URL. Por favor, inclua um token válido.",
            "status": "401"
        }
    
    return jsonify(response)
  
@app.route('/nomev1')
def nome():
    user_ip = request.remote_addr
    log_activity(user_ip, '/nomev1')
    
    # Obtenha o token da query string
    token = request.args.get('token')
    
    if token is not None:
        # Verifique se o token existe no JSON de tokens
        if token in tokens:
            query = request.args.get('query')
            if query is not None:
                re = requests.get(f'http://nexus.vortexuscloud.com:4144/nome?query={query}&token=EuSouPika')
                rr = re.json()
                msg = rr.get('msg')
                if msg == "Nome não encontrado":
                  return "Não encontrado."
                res = rr.get('resultado')
                nome = res.get('Nome')
                cpf = res.get('Cpf_cnpj')
                nasci = res.get('Nascimento')
                mae = res.get('mae')
                if res is not None:
                    return f"👥 CONSULTA NOME RECEITA 👥\n\nNOME: {nome}\nCPF - CNPJ: {cpf}\nNASCIMENTO: {nasci}\nMAE: {mae}"
                else:
                    response = {
                        "erro": "Não foi possível obter o resultado.",
                        "status": "404"
                    }
            else:
                response = {
                    "erro": "Parâmetro ?query= não foi fornecido na URL.",
                    "status": "404"
                }
        else:
            response = {
                "erro": "Token inválido.",
                "status": "401"
            }
    else:
        response = {
            "erro": "Token não fornecido na URL. Por favor, inclua um token válido.",
            "status": "401"
        }
    
    return jsonify(response)

@app.route('/nomev2')
def nome2():
    user_ip = request.remote_addr
    log_activity(user_ip, '/nomev2')
    
    # Obtenha o token da query string
    token = request.args.get('token')
    
    if token is not None:
        # Verifique se o token existe no JSON de tokens
        if token in tokens:
            query = request.args.get('query')
            if query is not None:
                re = requests.get(f'http://nexus.vortexuscloud.com:4144/nome2?query={query}&token=EuSouPika')
                rr = re.text
                res = rr.replace('{', '').replace('[', '').replace('}', '').replace(']', '').replace('"', '').replace('msg:', '').replace(',', '').replace('status:', '')
                if res is not None:
                    return f"👥 CONSULTA NOME DATAPRIME 👥\n\n{res}"
                else:
                    response = {
                        "erro": "Não foi possível obter o resultado.",
                        "status": "404"
                    }
            else:
                response = {
                    "erro": "Parâmetro ?query= não foi fornecido na URL.",
                    "status": "404"
                }
        else:
            response = {
                "erro": "Token inválido.",
                "status": "401"
            }
    else:
        response = {
            "erro": "Token não fornecido na URL. Por favor, inclua um token válido.",
            "status": "401"
        }
    
    return jsonify(response)
  
@app.route('/cpfv1')
def cpf1():
    user_ip = request.remote_addr
    log_activity(user_ip, '/cpfv1')
    
    # Obtenha o token da query string
    token = request.args.get('token')
    
    if token is not None:
        # Verifique se o token existe no JSON de tokens
        if token in tokens:
            query = request.args.get('query')
            if query is not None:
                re = requests.get(f'http://nexus.vortexuscloud.com:4144/cpf?query={query}&token=EuSouPika')
                rr = re.json()
                msg = rr.get('msg')
                if msg == "cpf não encontrado":
                  return "Não encontrado."
                res = rr.get('resultado')
                cpf = res.get('cpf')
                pis = res.get('pis')
                eel = res.get('titulo_eleitor')
                res2 = res.get('rg')
                rg = res2.get('rg')
                dtaex = res2.get('data_expedicao')
                org = res2.get('orgao_expedidor')
                uf = res2.get('uf_rg')
                res3 = res.get('dados_pessoais')
                nome = res3.get('nome')
                idade = res3.get('idade')
                nascimento = res3.get('nascimento')
                signo = res3.get('signo')
                nascii = res3.get('nacionalidade')
                escc = res3.get('escolaridade')
                esttsv = res3.get('estado_civil')
                profis = res3.get('profissao')
                renda = res3.get('renda')
                stts = res3.get('status_receita_federal')
                res4 = res.get('filiacao')
                mae = res4.get('mae')
                pai = res4.get('pai')
                if res is not None:
                    return f"🔍 CONSULTA CPF SERASA 🔍\n\nCPF: {cpf}\nPIS: {pis}\nTITULO DE ELEITOR: {eel}\nRG: {rg}\nDATA EXPEDIÇÃO: {dtaex}\nORGÃO EXPEDIDOR: {org}\nUF - RG: {uf}\nNOME: {nome}\nNASCIMENTO: {nascimento}\nIDADE: {idade}\nNASCIONALIDADE: {nascii}\nESCOLARIDADE: {escc}\nESTADO CIVIL: {esttsv}\nPROFISSÃO: {profis}\nRENDA: {renda}\nSTATUS RECEITA: {stts}\nMAE: {mae}\nPAI: {pai}"
                else:
                    response = {
                        "erro": "Não foi possível obter o resultado.",
                        "status": "404"
                    }
            else:
                response = {
                    "erro": "Parâmetro ?query= não foi fornecido na URL.",
                    "status": "404"
                }
        else:
            response = {
                "erro": "Token inválido.",
                "status": "401"
            }
    else:
        response = {
            "erro": "Token não fornecido na URL. Por favor, inclua um token válido.",
            "status": "401"
        }
    
    return jsonify(response)

@app.route('/cpfv2')
def cpf2():
    user_ip = request.remote_addr
    log_activity(user_ip, '/cpfv2')
    
    # Obtenha o token da query string
    token = request.args.get('token')
    
    if token is not None:
        # Verifique se o token existe no JSON de tokens
        if token in tokens:
            query = request.args.get('query')
            if query is not None:
                re = requests.get(f'http://nexus.vortexuscloud.com:4144/cpf2?query={query}&token=EuSouPika')
                rr = re.json()
                msg = rr.get('msg')
                if msg == "cpf não encontrado":
                  return "Não encontrado."
                res = rr.get('resultado')
                cpf = res.get('cpf')
                sit = res.get('situacao')
                cns = res.get('cns')
                nome = res.get('nome')
                nascii = res.get('nascimento')
                sexo = res.get('sexo')
                mae = res.get('mae')
                pai = res.get('pai')
                obito = res.get('obito')
                conj = res.get('conjulge')
                est = res.get('estado_civil')
                nasci = res.get('nacionalidade')
                renda = res.get('renda')
                profis = res.get('profissao')
                esc = res.get('escolaridade')
                pda = res.get('poder_arquisitivo')
                csb = res.get('score_csb')
                fx = res.get('score_csb_faixa_risco')
                desc = res.get('descricao_mosaic')
                classe = res.get('classe_mosaic')
                rg = res.get('rg_numero')
                org = res.get('orgao_emissor')
                end = res.get('endereco')
                if res is not None:
                    return f"🔎 CONSULTA CPF OWNDATA 🔍\n\nCPF: {cpf}\nSITUACAO: {sit}\nCNS: {cns}\nNOME: {nome}\nNASCIMENTO: {nascii}\nSEXO: {sexo}\nMAE: {mae}\nPAI: {pai}\nOBITO: {obito}\nCONJULGE: {conj}\nESTADO CIVIL: {est}\nNASCIONALIDADE: {nasci}\nRENDA: {renda}\nPROFISSÃO: {profis}\nESCOLARIDADE: {esc}\nPODER ARQUISITIVO: {pda}\nSCORE - CSB: {csb}\nSCORE - CSB - FAIXA - RISCO: {fx}\nDESCRICAO - MOSAIC: {desc}\nCLASSE - MOSAIC: {classe}\nRG: {rg}\nORGAO - EMISSOR: {org}\nENDERECO: {end}"
                else:
                    response = {
                        "erro": "Não foi possível obter o resultado.",
                        "status": "404"
                    }
            else:
                response = {
                    "erro": "Parâmetro ?query= não foi fornecido na URL.",
                    "status": "404"
                }
        else:
            response = {
                "erro": "Token inválido.",
                "status": "401"
            }
    else:
        response = {
            "erro": "Token não fornecido na URL. Por favor, inclua um token válido.",
            "status": "401"
        }
    
    return jsonify(response)

@app.route('/cpfv3')
def cpf3():
    user_ip = request.remote_addr
    log_activity(user_ip, '/cpfv3')
    
    # Obtenha o token da query string
    token = request.args.get('token')
    
    if token is not None:
        # Verifique se o token existe no JSON de tokens
        if token in tokens:
            query = request.args.get('query')
            if query is not None:
                re = requests.get(f'http://nexus.vortexuscloud.com:4144/cpf3?query={query}&token=EuSouPika')
                rr = re.json()
                msg = rr.get('msg')
                if msg == "cpf não encontrado":
                  return "Não encontrado."
                res = rr.get('resultado')
                if res is not None:
                    return f"{res}"
                else:
                    response = {
                        "erro": "Não foi possível obter o resultado.",
                        "status": "404"
                    }
            else:
                response = {
                    "erro": "Parâmetro ?query= não foi fornecido na URL.",
                    "status": "404"
                }
        else:
            response = {
                "erro": "Token inválido.",
                "status": "401"
            }
    else:
        response = {
            "erro": "Token não fornecido na URL. Por favor, inclua um token válido.",
            "status": "401"
        }
    
    return jsonify(response)

@app.route('/cpfv4')
def rg():
    user_ip = request.remote_addr
    log_activity(user_ip, '/cpfv4')
    
    # Obtenha o token da query string
    token = request.args.get('token')
    
    if token is not None:
        # Verifique se o token existe no JSON de tokens
        if token in tokens:
            query = request.args.get('query')
            if query is not None:
                re = requests.get(f'http://nexus.vortexuscloud.com:4144/cpf4?query={query}&token=EuSouPika')
                rr = re.json()
                msg = rr.get('msg')
                if msg == "cpf não encontrado":
                  return "Não encontrado."
                res = rr.get('resultado')
                if res is not None:
                    return f"{res}"
                else:
                    response = {
                        "erro": "Não foi possível obter o resultado.",
                        "status": "404"
                    }
            else:
                response = {
                    "erro": "Parâmetro ?query= não foi fornecido na URL.",
                    "status": "404"
                }
        else:
            response = {
                "erro": "Token inválido.",
                "status": "401"
            }
    else:
        response = {
            "erro": "Token não fornecido na URL. Por favor, inclua um token válido.",
            "status": "401"
        }
    
    return jsonify(response)


# Run the Flask app on 'localhost' port '8080'
if __name__ == '__main__':
  serve(app, host='0.0.0.0', port=8855)
