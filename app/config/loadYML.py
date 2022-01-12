import yaml

applicationConfig = open("config/config.yml", "r")
data = yaml.safe_load(applicationConfig)

botPrefix = data["botPrefix"]