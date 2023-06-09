from bs4 import BeautifulSoup
import requests
# import pandas as pd

# df = pd.read_excel('logo.xlsx')
arr = [
    "Python",
"Java",
"C++",
"JavaScript",
"Ruby",
"C#",
"PHP",
"Swift",
"Kotlin",
"Go",
"HTML5",
"CSS3",
"React",
"Angular",
"Vue.js",
"Bootstrap",
"jQuery",
"RESTful APIs",
"GraphQL",
"Node.js",
"Express.js",
"Django",
"Ruby on Rails",
"ASP.NET",
"SQL",
"MySQL",
"PostgreSQL",
"Oracle",
"MongoDB",
"NoSQL",
"Git",
"GitHub",
"Docker",
"Kubernetes",
"AWS (Amazon Web Services)",
"Azure",
"Google Cloud Platform",
"Linux",
"Windows Server",
"Networking",
"TCP/IP",
"DNS",
"DHCP",
"Firewall configuration",
"Cybersecurity",
"Penetration testing",
"Ethical hacking",
"Data analysis",
"Machine learning",
"Artificial intelligence",
"Natural language processing",
"Big Data",
"Hadoop",
"Spark",
"Data visualization",
"Tableau",
"Power BI",
"MATLAB",
"R",
"Excel",
"Statistical analysis",
"Agile methodologies",
"Scrum",
"Kanban",
"Project management",
"UI/UX design",
"Adobe Creative Suite",
"Photoshop",
"Illustrator",
"InDesign",
"Front-end development",
"Back-end development",
"Mobile app development",
"Android",
"iOS",
"Swift",
"Objective-C",
"Kotlin",
"Flutter",
"React Native",
"Xamarin",
"Software testing",
"Test automation",
"Selenium",
"JUnit",
"DevOps",
"Continuous Integration/Continuous Deployment (CI/CD)",
"Jenkins",
"Ansible",
"Puppet",
"Chef",
"Technical writing",
"Documentation",
"Troubleshooting",
"Cryptography",
"Blockchain technology",
"Internet of Things (IoT)",
"Robotics",
"3D Printing",
"Augmented Reality (AR)",
"Virtual Reality (VR)",
"Cybersecurity Frameworks (e.g., NIST, ISO 27001)",
"Incident Response",
"Malware Analysis",
"Wireless Networking",
"Mobile Security",
"Reverse Engineering",
"Data Warehousing",
"Business Intelligence",
"Enterprise Resource Planning (ERP) Systems",
"Supply Chain Management (SCM)",
"ITIL (Information Technology Infrastructure Library)",
"IT Service Management (ITSM)",
"Shell Scripting",
"PowerShell",
"Web Servers (Apache, Nginx)",
"Microservices Architecture",
"Agile Software Development",
"Software Quality Assurance (SQA)",
"Test Planning",
"Load Testing",
"Usability Testing",
"Data Structures",
"Algorithms",
"Object-Oriented Programming (OOP)",
"Functional Programming",
"Version Control Systems (Git, SVN)",
"Data Modeling",
"Cloud Storage Solutions (AWS S3, Google Cloud Storage)",
"Serverless Computing",
"Containerization (Docker, Kubernetes)",
"CI/CD (Continuous Integration/Continuous Deployment)",
"Infrastructure as Code (IaC)",
"Network Protocols (TCP/IP, HTTP, SSL/TLS)",
"Microcontrollers (Arduino, Raspberry Pi)",
"Computer Architecture",
"System Design",
"Data Governance",
"Data Privacy",
"ETL (Extract, Transform, Load)",
"Business Analysis",
"Requirements Gathering",
"Software Documentation",
"Quality Assurance (QA)",
"User Acceptance Testing (UAT)",
"Scripting Languages (Bash, PowerShell, Perl)",
"Continuous Monitoring",
"Agile Project Management",
"Scrum Master",
"Data Cleansing",
"Predictive Modeling",
"Data Mining",
"Data Integration",
"Natural Language Generation (NLG)",
"Data Warehouse Design",
"Data Governance",
"Cloud Security",
"Network Security Auditing",
"Vulnerability Assessment",
"Security Incident Response",
"Threat Intelligence",
"Cryptocurrency",
"Distributed Ledger Technology",
"Software Architecture",
"Design Patterns",
"GraphQL",
"REST API Design",
"UX Research",
"Wireframing",
"Accessibility Testing",
"Responsive Design",
"Cross-Browser Testing",
"Performance Optimization",
"Code Review",
"Secure Coding Practices",
"Virtualization (VMware, Hyper-V)",
"Web Scraping",
"Business Process Improvement",
"Change Management",
"Database Administration",
"Disaster Recovery Planning",
"IT Governance",
"Risk Assessment",
"Systems Analysis",
"Data Visualization Tools (D3.js, Plotly, ggplot)",
"Statistical Modeling",
"Time Series Analysis",
"Data Analytics",
"Data Storytelling",
"Social Media Analytics",
"Cloud Migration",
"Server Administration (Linux, Windows)",
"Network Troubleshooting",
"Wireless Security",
"Intrusion Detection Systems (IDS)",
"Firewall Management",
"Incident Handling",
"Digital Forensics",
"Data Loss Prevention (DLP)",
"Secure SDLC (Software Development Life Cycle)",
"Data Governance",
"Cloud Architecture",
"Data Science",
"Statistical Analysis",
"Natural Language Generation (NLG)",
"Data Visualization",
"Machine Learning Algorithms",
"Neural Networks",
"Deep Learning",
"Computer Vision",
"Reinforcement Learning",
"Predictive Modeling",
"Time Series Analysis",
"A/B Testing",
"Recommender Systems",
"Data Preprocessing",
"Feature Engineering",
"Text Mining",
"Sentiment Analysis",
"Image Processing",
"Speech Recognition",
"Chatbot Development",
"Virtual Assistant Development",
"Data Pipelines",
"Data Cleaning",
"Data Transformation",
"Data Wrangling",
"Data Imputation",
"Data Augmentation",
"Anomaly Detection",
"Model Evaluation",
"Ensemble Learning",
"Dimensionality Reduction",
"Hyperparameter Tuning",
"Model Deployment",
"Natural Language Understanding (NLU)",
"Data Governance",
"Data Privacy",
"Data Ethics",
"Data Compliance",
"Data Security",
"Data Cataloging",
"Data Lineage",
"Data Access Control",
"Data Masking",
"Data Encryption",
"Data Auditing",
"Data Classification",
"Cloud Security",
"Network Security",
"Application Security",
"Identity and Access Management (IAM)",
"Security Architecture Design",
"Security Risk Assessment",
"Security Incident Response",
"Vulnerability Management",
"Threat Intelligence",
"Security Awareness Training",
"Secure Coding Practices",
"Security Testing",
"Cloud Governance",
"Cloud Monitoring",
"Cloud Cost Optimization",
"Serverless Computing",
"Infrastructure as Code (IaC)",
"Cloud Networking",
"Cloud Storage",
"Cloud Deployment Models (IaaS, PaaS, SaaS)",
"Cloud Migration Strategies",
"Server Administration (Windows, Linux)",
"Active Directory",
"Virtualization (VMware, Hyper-V)",
"Network Administration",
"Network Troubleshooting",
"Routing and Switching",
"Network Protocols (TCP/IP, DNS, DHCP)",
"Wireless Networking",
"Network Security",
"Firewall Configuration",
"Intrusion Detection Systems (IDS)",
"Virtual Private Networks (VPNs)",
"Software Development Lifecycle (SDLC)",
"Agile Methodologies (Scrum, Kanban)",
"Waterfall Methodology",
"Test-Driven Development (TDD)",
"Continuous Integration/Continuous Deployment (CI/CD)",
"DevOps Tools (Jenkins, GitLab, CircleCI)",
"Configuration Management (Ansible, Puppet, Chef)",
"Containerization (Docker, Kubernetes)",
"Microservices Architecture",
"API Design and Development",
"Web Services (SOAP, REST)",
"GraphQL",
"Message Queueing (RabbitMQ, Kafka)",
"Event-Driven Architecture",
"Serverless Computing",
"Performance Optimization",
"Load Testing",
"Code Review",
"Code Refactoring",
"Cloud Orchestration",
"Serverless Architecture",
"Serverless Frameworks (AWS Lambda, Azure Functions)",
"Data Engineering",
"Data Governance",
"Data Streaming",
"Real-time Analytics",
"Data Lake",
"Data Warehouse",
"Data Migration",
"Data Governance",
"Data Cataloging",
"Data Lineage",
"Data Quality Management",
"Master Data Management (MDM)",
"Data Privacy Compliance (GDPR, CCPA)",
"Data Ethics",
"Blockchain Development",
"Smart Contracts",
"Decentralized Applications (dApps)",
"Cryptocurrency Wallets",
"Solidity Programming",
"Hyperledger Fabric",
"Computer Networks",
"Network Protocols (HTTP, SSL/TLS, DNS)",
"Network Monitoring",
"Wireless Security",
"Network Virtualization",
"Software Defined Networking (SDN)",
"Network Automation",
"Firewall Configuration and Management",
"Intrusion Detection and Prevention Systems (IDPS)",
"Vulnerability Assessment and Penetration Testing (VAPT)",
"Security Information and Event Management (SIEM)",
"Security Incident Response",
"Security Auditing and Compliance",
"Security Risk Assessment",
"Web Application Security",
"Malware Analysis and Reverse Engineering",
"Security Operations Center (SOC)",
"Cloud Native Development",
"Infrastructure as Code (IaC) Tools (Terraform, CloudFormation)",
"Cloud Automation",
"Cloud Monitoring and Management",
"Server Administration (Windows, Linux)",
"System Administration",
"IT Service Management (ITSM)",
"Incident Management",
"Change Management",
"Configuration Management",
"Performance Monitoring and Optimization",
"Database Administration (SQL, NoSQL)",
"Data Backup and Recovery",
"Disaster Recovery Planning",
"Data Center Operations",
"IT Asset Management",
"ITIL Framework",
"IT Governance and Compliance",
"Business Process Automation",
"Robotic Process Automation (RPA)",
"Natural Language Generation (NLG)",
"Conversational AI",
"Speech Recognition and Synthesis",
"Emotion Recognition",
"Image Recognition",
"Reinforcement Learning",
"Genetic Algorithms",
"Data Mining",
"Recommendation Systems",
"Text Classification",
"Sentiment Analysis",
"Fraud Detection",
"Marketing Analytics",
"Predictive Maintenance",
"Data Wrangling",
"Data Visualization (Tableau, Power BI, D3.js)",
"Statistical Modeling",
"Experiment Design and Analysis",
"Data Storytelling",
"Agile Project Management",
"Scrum",
"Kanban",
"Lean Software Development",
"Requirements Gathering and Analysis",
"User Experience (UX) Design",
"User Interface (UI) Design",
"Wireframing and Prototyping",
"Usability Testing",
"Responsive Web Design",
"Mobile App Design",
"Cross-Platform Development",
"Test Planning and Strategy",
"Test Automation",
"Performance Testing",
"Security Testing",
"User Acceptance Testing (UAT)",
"Continuous Integration/Continuous Deployment (CI/CD)",
"Version Control Systems (Git, SVN)",
"Agile Tools (Jira, Trello, Asana)",
"Technical Documentation",
"Jira",
"Confluence",
"Trello",
"Asana",
"Slack",
"Microsoft Office Suite (Word, Excel, PowerPoint)",
"Google Suite (Docs, Sheets, Slides)",
"SharePoint",
"GitHub",
"GitLab",
"Bitbucket",
"Jenkins",
"Travis CI",
"CircleCI",
"SonarQube",
"Selenium",
"Appium",
"Postman",
"SoapUI",
"JUnit",
"NUnit",
"PyTest",
"Mocha",
"Chai",
"Cypress",
"JMeter",
"LoadRunner",
"New Relic",
"Splunk",
"Grafana",
"Kibana",
"Nagios",
"Zabbix",
"Wireshark",
"Burp Suite",
"Metasploit",
"Nessus",
"Qualys",
"Snort",
"OWASP",
"Wi-Fi Analyzer",
"SQL Server Management Studio (SSMS)",
"Oracle SQL Developer",
"MySQL Workbench",
"PostgreSQL",
"MongoDB Compass",
"Apache Kafka",
"RabbitMQ",
"Elasticsearch",
"Redis",
"Docker",
"Kubernetes",
"Ansible",
"Puppet",
"Chef",
"Vagrant",
"Terraform",
"Amazon Web Services (AWS)",
"Microsoft Azure",
"Google Cloud Platform (GCP)",
"Microsoft Visual Studio",
"Eclipse",
"IntelliJ IDEA",
"PyCharm",
"Sublime Text",
"Atom",
"Visual Studio Code",
"Photoshop",
"Illustrator",
"InDesign",
"Sketch",
"Figma",
"Adobe XD",
"AutoCAD",
"SolidWorks",
"MATLAB",
"RStudio",
"Tableau",
"Power BI",
"Google Analytics",
"Google Tag Manager",
"Adobe Analytics",
"Salesforce",
"SAP",
"SharePoint",
"WordPress",
"Drupal",
"Magento",
"WooCommerce",
"Shopify",
"Joomla",
"Apache HTTP Server",
"Nginx",
"Microsoft IIS",
"Apache Tomcat",
"Express.js",
"Spring Framework",
"Ruby on Rails",
"Flask",
"Laravel",
"Atlassian Jira",
"Atlassian Confluence",
"Basecamp",
"Microsoft Project",
"Wrike",
"Zendesk",
"ServiceNow",
"Monday.com",
"Evernote",
"Dropbox",
"Google Drive",
"Microsoft SharePoint",
"Git",
"Mercurial",
"SVN (Subversion)",
"Perforce",
"Artifactory",
"Gradle",
"Maven",
"TeamCity",
"Bamboo",
"Bitbucket Pipelines",
"AWS CodePipeline",
"Azure DevOps",
"Selenium WebDriver",
"Cucumber",
"TestComplete",
"LoadUI",
"LoadNinja",
"Apache JMeter",
"Gatling",
"BlazeMeter",
"AppDynamics",
"Datadog",
"New Relic APM",
"Splunk Enterprise",
"ELK Stack (Elasticsearch, Logstash, Kibana)",
"Graylog",
"Prometheus",
"Grafana",
"Nagios XI",
"PRTG Network Monitor",
"SolarWinds Orion",
"Wireshark",
"tcpdump",
"QualysGuard",
"Rapid7 Nexpose",
"Fortify",
"OWASP ZAP",
"McAfee SecurityCenter",
"Cisco ASA",
"Palo Alto Networks Firewall",
"F5 BIG-IP",
"Snort IDS/IPS",
"Imperva WAF",
"Nessus",
"ArcSight",
"AlienVault USM",
"Wi-Fi Analyzer",
"AirMagnet Survey",
"SQL Server Management Studio (SSMS)",
"Oracle SQL Developer",
"MySQL Workbench",
"Toad for Oracle",
"pgAdmin",
"MongoDB Compass",
"Robo 3T",
"Apache Kafka",
"Apache NiFi",
"RabbitMQ",
"ActiveMQ",
"Elasticsearch",
"Kibana",
"Logstash",
"Redis",
"Docker Compose",
"Rancher",
"Ansible Tower",
"SaltStack",
"Puppet Enterprise",
"Jenkins X",
"AWS CloudFormation",
"Google Cloud Deployment Manager",
"Packer",
"Amazon S3",
"Google Cloud Storage",
"Azure Blob Storage",
"HashiCorp Vault",
"Microsoft Active Directory",
"Okta",
"OneLogin",
"Ping Identity",
"LDAP (Lightweight Directory Access Protocol)",
"OAuth",
"SAML (Security Assertion Markup Language)",
"OpenID Connect",
"F5 BIG-IP",
"NGINX Plus",
"HAProxy",
"Akamai CDN",
"Elastic Beanstalk",
"Heroku",
"App Engine",
"Firebase",
"Apache Tomcat",
"Jetty",
"WildFly (JBoss)",
"Express.js",
"Nest.js",
"Flask",
"Django",
"Ruby on Rails",
"Laravel",
"Spring Boot",
"ASP.NET",
"GraphQL",
"RESTful API",
"SOAP",
"XML",
"JSON",
"OAuth 2.0",
"OpenAPI (Swagger)",
"RAML (RESTful API Modeling Language)",
"GraphQL",
"User Experience (UX) Design",
"User Interface (UI) Design",
"Wireframing",
"Prototyping",
"User Research",
"Usability Testing",
"Responsive Web Design",
"Mobile App Design",
"Design Thinking",
"A/B Testing",
"Google Analytics",
"Adobe Analytics",
"Mixpanel",
"Salesforce CRM",
"SAP ERP",
"HubSpot",
"WordPress CMS",
"Drupal CMS",
"Magento eCommerce",
"WooCommerce",
"Shopify",
"Joomla CMS",
"Apache Web Server",
"NGINX",
"Microsoft IIS",
"CloudFront (AWS CDN)",
"Akamai CDN",
"WordPress Speed Optimization",
"Search Engine Optimization (SEO)",
"Google Ads",
"Facebook Ads",
"LinkedIn Ads",
"Twitter Ads",
"Google Tag Manager",
"Firebase Analytics",
"Adobe Creative Cloud",
"Salesforce Marketing Cloud",
"Marketo",
"Mailchimp",
"Hootsuite",
"Google Ads",
"Facebook Ads Manager",
"LinkedIn Campaign Manager",
"Twitter Ads",
"SEMrush",
"Moz",
"Salesforce Sales Cloud",
"SAP Sales Cloud",
"Microsoft Dynamics 365",
"Zendesk Support",
"Freshdesk",
"Intercom",
"Slack API",
"Twilio",
"SendGrid",
"Stripe",
"PayPal",
"Braintree",
"WooCommerce Payments",
"Shopify Payments",
"Authorize.Net",
"WordPress Plugin Development",
"Drupal Module Development",
"Magento Extension Development",
"WordPress Theme Development",
"Joomla Extension Development",
"GitLab CI/CD",
"Team Foundation Server (TFS)",
"Octopus Deploy",
"AWS Lambda",
"Google Cloud Functions",
"Azure Functions",
"Serverless Framework",
"Terraform",
"AWS CloudFormation",
"Google Cloud Dployment Manager",
"Amazon DynamoDB",
"",
"Google Cloud Bigtable",
"Azure Cosmos DB",
"MySQL Replication",
"PostgreSQL Replication",
"MongoDB Replication",
"Oracle Data Guard",
"SQL Server Always On Availability Groups",
"Redis Cluster",
"Neo4j Graph Database",
"Apache Cassandra",
"Couchbase",
"Oracle WebLogic Server",
"IBM WebSphere Application Server",
"Apache Tomcat",
"NGINX",
"Microsoft IIS",
"JavaServer Pages (JSP)",
"JavaServer Faces (JSF)",
"Apache Struts",
"ASP.NET",
"Ruby on Rails",
"Django",
"Laravel",
"Spring Boot",
"Apache Wicket",
"AngularJS",
"React",
"Vue.js",
"Ember.js",
"Flutter",
"Swift",
"Kotlin",
"Xamarin",
"Apache Hadoop",
"Apache Spark",
"Apache Flink",
"Apache Beam",
"Apache NiFi",
"TensorFlow",
"PyTorch",
"Keras",
"scikit-learn",
"OpenCV",
"Natural Language Processing (NLP)",
"Computer Vision",
"Deep Learning",
"Reinforcement Learning",
"Genetic Algorithms",
"Image Recognition",
"Speech Recognition",
"Chatbot Development",
"Recommendation Systems",
"Data Mining",
"Time Series Analysis",
"Anomaly Detection",
"Statistical Modeling",
"Bayesian Inference",
"Experiment Design and Analysis",
"Data Visualization",
"Tableau",
"Power BI",
"QlikView",
"D3.js",
"Plotly",
"Matplotlib",
"ggplot2",
"Agile Project Management",
"Scrum",
"Kanban",
"Lean Software Development",
"DevOps",
"Continuous Integration/Continuous Deployment (CI/CD)",
"Jenkins",
"Travis CI",
"CircleCI",
"GitLab CI/CD",
"AWS CodePipeline",
"Google Cloud Build",
"Azure DevOps",
"Docker",
"Kubernetes",
"Amazon Elastic Kubernetes Service (EKS)",
"Google Kubernetes Engine (GKE)",
"Azure Kubernetes Service (AKS)",
"Helm",
"Istio",
"Prometheus",
"Grafana",
"Splunk",
"ELK Stack (Elasticsearch, Logstash, Kibana)",
"Graylog",
"Zabbix",
"Nagios",
"AppDynamics",
"New Relic",
"Dynatrace",
"Azure Monitor",
"AWS CloudWatch",
"Datadog",
"HashiCorp Terraform",
"AWS CloudFormation",
"Azure Resource Manager (ARM)",
"Google Cloud Deployment Manager",
"Ansible",
"Puppet",
"Chef",
"SaltStack",
"Jenkins X",
"GitOps",
"AWS Lambda",
"Azure Functions",
"Google Cloud Functions",
"AWS Step Functions",
"Apache Airflow",
"Serverless Framework",
"AWS API Gateway",
"Azure API Management",
"Google Cloud Endpoints",
"Kong",
"OAuth",
"OpenID Connect",
"SAML",
"JWT (JSON Web Tokens)",
"OAuth 2.0",
"OpenAPI (Swagger)",
"gRPC",
"GraphQL",
"SOAP",
"RES",
"Service Mesh (e.g., Istio, Linkerd)",
"Event-Driven Architecture",
"Message Queueing (e.g., RabbitMQ, Apache Kafka)",
"Service-Oriented Architecture (SOA)",
"Reactive Programming",
"API Design and Development",
"Secure Coding Practices",
"OWASP Top 10",
"Penetration Testing",
"Security Incident and Event Management (SIEM)",
"Identity and Access Management (IAM)",
"Cloud Security",
"Data Encryption",
"Security Auditing and Compliance",
"Secure SDLC",
"ITIL (Information Technology Infrastructure Library)",
"Service Desk Management",
"Incident Management",
"Change Management",
"Problem Management",
"Release Management",
"IT Asset Management",
"IT Service Continuity Management",
"IT Service Level Management",
"IT Capacity Planning",
"IT Configuration Management",
"IT Operations Management",
"IT Governance",
"IT Risk Management",
"IT Compliance",
"Business Intelligence (BI)",
"Data Warehousing",
"ETL (Extract, Transform, Load)",
"Data Cleansing",
"Data Integration",
"Data Modeling",
"Data Governance",
"Data Quality Management",
"Data Mining",
"Business Analytics",
"Predictive Analytics",
"Prescriptive Analytics",
"Descriptive Analytics",
"Data Visualization",
"Machine Learning",
"Artificial Intelligence",
"Natural Language Processing (NLP)",
"Image Recognition",
"Speech Recognition",
"Pattern Recognition",
"Recommendation Systems",
"Sentiment Analysis",
"Neural Networks",
"Deep Learning",
"Reinforcement Learning",
"Genetic Algorithms",
"Data Science",
"Statistical Analysis",
"Hypothesis Testing",
"A/B Testing",
"Experimental Design",
"Time Series Analysis",
"Regression Analysis",
"Classification Models",
"Cluster Analysis",
"Dimensionality Reduction",
"Data Preprocessing",
"Feature Selection",
"Feature Engineering",
"Big Data",
"Hadoop",
"Spark",
"MapReduce",
"HDFS (Hadoop Distributed File System)",
"Hive",
"Pig",
"HBase",
"Cassandra",
"Storm",
"Sqoop",
"Flume",
"Kafka",
"NoSQL Databases",
"MongoDB",
"Cassandra",
"Couchbase",
"DynamoDB",
"Redis",
"Neo4j",
"InfluxDB",
"Time Series Databases",
"Graph Databases",
"Apache Lucene",
"ElasticSearch",
"Solr",
"Kibana",
"Logstash",
"Flink",
"Data Engineering",
"Data Pipelines",
"Data Integration",
"Data Lakes",
"Data Governance",
"Extract, Transform, Load (ETL)",
"Stream Processing",
"Workflow Orchestration",
"Cloud Computing",
"Amazon Web Services (AWS)",
"Microsoft Azure",
"Google Cloud Platform (GCP)",
"Virtualization",
"VMware",
"Hyper-V",
"KVM",
"Xen",
"Infrastructure as Code (IaC)",
"Configuration Management",
"Disaster Recovery",
"High Availability",
"Load Balancing",
"Network Security",
"VPN (Virtual Private Network)",
"Firewalls",
"Intrusion Detection and Prevention Systems (IDS/IPS)",
"SIEM (Security Information and Event Management)",
"Security Auditing",
"Encryption",
"PKI (Public Key Infrastructure)",
"Data Loss Prevention (DLP)",
"Incident Response",
"Malware Analysis",
"Vulnerability Assessment",
"Penetration Testing",
"Identity and Access Management (IAM)",
"Single Sign-On (SSO)",
"Active Directory",
"LDAP (Lightweight Directory Access Protocol)",
"Network Administration",
"Routing and Switching",
"Network Protocols (TCP/IP, DNS, DHCP, etc.)",
"Wireless Networking",
"Network Monitoring and Analysis",
"Network Troubleshooting",
"Firewall Configuration and Management",
"Cloud Networking",
"SD-WAN (Software-Defined Wide Area Network)",
"VoIP (Voice over Internet Protocol)",
"Collaboration Tools",
"Microsoft Office 365",
"G Suite",
"Slack",
"Microsoft Teams",
"Zoom",
"WebEx",
"Asana",
"Trello",
"Monday.com",
"Wrike",
"Jira",
"Confluence",
"GitLab",
"GitHub",
"Bitbucket",
"DevOps Tools",
"Configuration Management (Ansible, Puppet, Chef, SaltStack)",
"Continuous Integration/Continuous Deployment (Jenkins, Travis CI, CircleCI)",
"Containerization (Docker, Kubernetes)",
"Infrastructure Monitoring (Prometheus, Grafana, Splunk)",
"Agile Project Management (Scrum, Kanban, Lean)",
"Test Automation (Selenium, Appium, Postman)"
]
with open(f"data-1000.json", "a") as f:
        f.write("[")
        f.write("\n")
for i in arr:
    try:
        name = i + " logo"
        url = "https://www.google.com/search?q="+name+"&tbm=isch"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        image = soup.find("img", {"class": "yWs4tf"})
        link = image["src"]
        img_data = requests.get(link).content
        json = {
            "name": i,
            "link": link
        }
        print("Saving " + i + " logo")
        with open(f"data-1000.json", "a") as f:
            f.write(str(json))
            f.write(",")
            f.write("\n")
    except:
        print("Error saving " + i + " logo")
        json = {
            "name": i,
            "link": "error"
        }
        with open(f"data-1000.json", "a") as f:
            f.write(str(json))
            f.write(",")
            f.write("\n")
with open(f"data-1000.json", "a") as f:
        f.write("]")
        f.write("\n")