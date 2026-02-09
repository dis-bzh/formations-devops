from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.container import Docker
from diagrams.onprem.network import Internet, Nginx
from diagrams.onprem.mlops import Mlflow
from diagrams.generic.network import VPN
from diagrams.generic.os import Ubuntu
from diagrams.generic.database import SQL
from diagrams.saas.chat import Slack
from diagrams.programming.framework import Flask
from diagrams.custom import Custom

# Diagram 1: Architecture simple - Hello World (my-app)
with Diagram("Architecture Hello World - VM Unique", show=False, direction="TB", filename="architecture_helloworld"):
    with Cluster("Denv-r Cloud"):
        with Cluster("VM Workshop"):
            nginx = Nginx("Nginx\n:80")
            app = Docker("my-app\nNext.js\n:3000")
            nginx >> app

    internet = Internet("HTTP/HTTPS")
    internet >> nginx

    ssh = Internet("SSH (22)")
    bastion = VPN("Bastion")
    ssh >> bastion >> nginx


# Diagram 2: Architecture Capstone - Plateforme IA Sécurisée
with Diagram("Architecture Capstone - Plateforme IA Sécurisée", show=False, direction="LR", filename="architecture_capstone"):
    with Cluster("Denv-r Cloud"):
        with Cluster("VM Workshop"):
            with Cluster("Docker Compose"):
                nginx = Nginx("Nginx\n:80\nRate Limit\nSecurity Headers")
                gateway = Flask("Gateway\n:4000\nFail-Safe")
                anonymizer = Flask("Anonymizer\n:5001\nScrubadub + Regex")
                litellm = Docker("LiteLLM\n:4000\nProxy LLM")
                
                nginx >> Edge(label="OpenAI API") >> gateway
                gateway >> Edge(label="Anonymize") >> anonymizer
                gateway >> Edge(label="Forward") >> litellm

    # External LLMs
    with Cluster("Cloud LLM APIs"):
        openai = Slack("OpenAI\nGPT-3.5/4")
        claude = Slack("Anthropic\nClaude")
        gemini = Slack("Google\nGemini")
    
    litellm >> Edge(color="blue") >> openai
    litellm >> Edge(color="orange") >> claude
    litellm >> Edge(color="green") >> gemini

    # Clients
    cline = Internet("VS Code\n+ Cline")
    curl = Internet("curl / API")
    
    cline >> Edge(label="localhost:80") >> nginx
    curl >> nginx


# Diagram 3: Architecture Multi-VM (production)
with Diagram("Architecture Cloud Native - Production Multi-VM", show=False, direction="LR", filename="architecture_production"):
    with Cluster("Denv-r Cloud"):
        with Cluster("Bastion"):
            bastion = VPN("SSH Access")
        
        with Cluster("Frontend / Gateway"):
            waf = Nginx("Nginx WAF\nRate Limit")
            gateway = Flask("Gateway\nAnonymizer")

        with Cluster("Backend AI"):
            litellm = Docker("LiteLLM")
            
        with Cluster("App Servers"):
            app1 = Ubuntu("App-1")
            app2 = Ubuntu("App-2")

        with Cluster("Database"):
            db = SQL("PostgreSQL")

    # External
    ssh = Internet("SSH (22)")
    ssh >> Edge(color="red") >> bastion >> Edge(color="red") >> waf
    
    web = Internet("HTTP/HTTPS")
    web >> Edge(color="darkgreen") >> waf >> Edge(color="darkgreen") >> gateway >> litellm
    waf >> Edge(label="/app") >> app1
    app1 >> db
    app2 >> db
    
    # LLMs
    with Cluster("Cloud LLMs"):
        llms = Slack("OpenAI/Claude/Gemini")
    litellm >> llms