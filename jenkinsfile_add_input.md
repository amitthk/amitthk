```groovy
stage 'promotion'
def userInput = input(
 id: 'userInput', message: 'Let\'s promote?', parameters: [
 [$class: 'TextParameterDefinition', defaultValue: 'uat', description: 'Environment', name: 'env'],
 [$class: 'TextParameterDefinition', defaultValue: 'uat1', description: 'Target', name: 'target']
])
echo ("Env: "+userInput['env'])
echo ("Target: "+userInput['target'])
```

and the result will be
Running: promotion
Entering stage promotion
Proceeding
Running: Input
Input requested
Running: Print Message
Env: uat
Running: Print Message
Target: uat1
Running: End of Workflow
Finished: SUCCESS
If you have only one parameter, its value will be directly returned instead of a Map

```groovy
stage 'promotion'
def userInput = input(
 id: 'userInput', message: 'Let\'s promote?', parameters: [
 [$class: 'TextParameterDefinition', defaultValue: 'uat', description: 'Environment', name: 'env']
])
echo ("Env: "+userInput)
```