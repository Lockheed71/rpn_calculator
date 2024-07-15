# coding: utf-8


from app.main import app

import uvicorn
import argparse


parser = argparse.ArgumentParser(
	prog='RPN api',
	description='Configuration des paramètre de lancement du service d\'api RPN'
)

parser.add_argument(
	'--host',
	type=str,
	default='127.0.0.1'
)

parser.add_argument(
	'--port',
	type=int,
	default=8000
)

parser.add_argument(
	'-r', '--reload',
	action='store_true'
)

if __name__ == '__main__':
	
	args = parser.parse_args()

	print(args)

	uvicorn.run('server:app', host=args.host, port=args.port, reload=args.reload)
