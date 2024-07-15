# coding: utf-8


from fastapi import APIRouter, HTTPException
import app.services as rpn_ops

rpn_router = APIRouter()

@rpn_router.get('/get', response_model=float)
def rpn_get_item():

	if rpn_ops.stack_len() < 1:
		raise HTTPException(status_code=400, detail='La pile est vide')

	return rpn_ops.stack_get()

@rpn_router.get('/stack', response_model=list)
def rpn_get_items():
	return rpn_ops.stack_get_stack()

@rpn_router.post('/push/{value}', response_model=float)
def rpn_push_item(value: float):
	return rpn_ops.stack_push(value)

@rpn_router.post('/pop', response_model=float)
def rpn_pop_item():
	if rpn_ops.stack_len() < 1:
		raise HTTPException(status_code=400, detail='La pile est vide')
	
	return rpn_ops.stack_pop()

@rpn_router.post('/clear')
def rpn_clear_items():
	return rpn_ops.stack_clear()

@rpn_router.post('/addition')
def rpn_ops_addition():
	if rpn_ops.stack_len() < 2:
		raise HTTPException(status_code=400, detail='La pile doit contenir au moins 2 éléments')

	return rpn_ops.stack_addition()

@rpn_router.post('substract')
def rpn_ops_substract():
	if rpn_ops.stack_len() < 2:
		raise HTTPException(status_code=400, detail='La pile doit contenir au moins 2 éléments')

	return rpn_ops.stack_substract()

@rpn_router.post('/multiply')
def rpn_ops_multiply():
	if rpn_ops.stack_len() < 2:
		raise HTTPException(status_code=400, detail='La pile doit contenir au moins 2 éléments')

	return rpn_ops.stack_multiply()

@rpn_router.post('/divide')
def rpn_ops_divide():
	try:
		return rpn_ops.stack_divide()
	except IndexError:
		raise HTTPException(status_code=400, detail='La pile doit contenir au moins 2 éléments')
	except ZeroDivisionError:
		raise HTTPException(status_code=400, detail='Impossible de diviser par zéro')
