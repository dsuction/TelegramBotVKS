from environs import Env

env = Env()
env.read_env()
TOKEN_API = env.str("TOKEN_API")
