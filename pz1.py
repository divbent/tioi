from random import choice, shuffle, randint
from time import time

def generate_simple_rules(code_max, n_max, n_generate, log_oper_choice=["and","or","not"]):
	rules = []
	if n_max < 2:
		n_max = 2
	for j in range(0, n_generate):
	    log_oper = choice(log_oper_choice)  #not means and-not (neither)
	    n_items = randint(2,n_max)
	    items = []
	    for i in range(0,n_items):
		    items.append( randint(1,code_max) )
	    rule = {
	          'if':{
	              log_oper:	 items         
	           },
	           'then':code_max+j
	        }
	    rules.append(rule)
	#shuffle(rules)
	return(rules)

def generate_stairway_rules(code_max, n_max, n_generate, log_oper_choice=["and","or","not"]):
	rules = []
	if n_max < 2:
		n_max = 2
	for j in range(0, n_generate):
	    log_oper = choice(log_oper_choice)  #not means and-not (neither)
	    n_items = randint(2,n_max)
	    items = []
	    for i in range(0,n_items):
		    items.append( i+j )
	    rule = {
	          'if':{
	              log_oper:	 items         
	           },
	           'then':i+j+1
	        }
	    rules.append(rule)
	#shuffle(rules)
	return(rules)

def generate_ring_rules(code_max, n_max, n_generate, log_oper_choice=["and","or","not"]):
	rules = generate_stairway_rules(code_max, n_max, n_generate -1, log_oper_choice)
	log_oper = choice(log_oper_choice)  #not means and-not (neither)
	if n_max < 2:
	    n_max = 2
	n_items = randint(2,n_max)
	items = []
	for i in range(0,n_items):
	    items.append( code_max-i )
	rule = {
	       'if':{
	          log_oper:	 items         
	       },
	       'then':0
	       }
	rules.append(rule)
	shuffle(rules)
	return(rules)			

def generate_random_rules(code_max, n_max, n_generate, log_oper_choice=["and","or","not"]):
	rules = []
	if n_max < 2:
	    n_max = 2
	for j in range(0, n_generate):
	    log_oper = choice(log_oper_choice)  #not means and-not (neither)
	    n_items = randint(2,n_max)
	    items = []
	    for i in range(0,n_items):
		    items.append( randint(1,code_max) )
	    rule = {
	          'if':{
	              log_oper:	 items         
	           },
	           'then':randint(1,code_max)
	        }
	    rules.append(rule)
	shuffle(rules)
	return(rules)

def generate_seq_facts(M):
	facts = list(range(0,M))
	shuffle(facts)
	return facts

def generate_rand_facts(code_max, M):
	facts = []
	for i in range(0,M):
		facts.append( randint(0, code_max) )
	return facts


#samples:
#print(generate_simple_rules(100, 4, 10))
#print(generate_random_rules(100, 4, 10))
#print(generate_stairway_rules(100, 4, 10, ["or"]))
#print(generate_ring_rules(100, 4, 10, ["or"]))

#generate rules and facts and check time
time_start = time()
N = 100000
M = 1000
#rules = generate_simple_rules(100,4,N)
rules = generate_stairway_rules(100, 4, N)
facts = generate_rand_facts(100, M)
facts = set(facts)
answer = list(facts)
lenanswer = 0


print("%d rules generated in %f seconds" % (N,time()-time_start))

#load and validate rules
# YOUR CODE HERE

#check facts vs rules
time_start = time()

#if lenanswer <= 100:
#	for rule in rules:
#		if 'and' in rule['if'] or 'or' in rule['if']:
#			answer.append(rule['then'])
#else:

while lenanswer != len(answer):
	lenanswer = len(answer)
	for rule in rules:
		if 'and' in rule['if']:
			for i in (rule['if']['and']):
				if not i in facts:
					break
			else:
				answer.append(rule['then'])
		if 'or' in rule['if']:
			for i in (rule['if']['or']):
				if  i in facts:
					answer.append(rule['then'])
					break
	facts = set(answer)
	answer = list(facts)

for rule in rules:
	if 'not' in rule['if']:
		for i in (rule['if']['not']):
			if  i in facts:
				break
		else:
			answer.append(rule['then'])


print(len(answer))

#print(rules[:100:])
#print(answer[100:200:])
print("%d facts validated vs %d rules in %f seconds" % (M,N,time()-time_start))