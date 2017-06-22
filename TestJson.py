from bottle import route, run, os, sys, request, Bottle
import functools
import moveRobo

@route('/instruction/')
def recipes_list():
    return { "success" : False, "paths" : [], "error" : "instruction not implemented yet" }

@route('/instruction/<script>/<args>', method='GET')
def passInstruction(script, args):
    print (script)
    print (args)
    x = os.system('./'+script+ ' ' + args)
    print (x)
    if x > 0:
        return "FAILURE"
    else:
        return "SUCCESS"


run(host='localhost', port=9099, debug=True)