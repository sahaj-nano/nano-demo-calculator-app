<p align="center">
<img src="http://nano.sahaj.ai/27ad2091b1714f583886.png" width="320" height="162" alt="Logo" title="NaN(O) logo">
</p>

## What is NaN(O)  
      
At Sahaj, tech consultants operate at the intersection between engineering and art. Simply put, they are artisans who take on complex engineering problems in the software industry across a wide spectrum of domains. Their work is deeply rooted in first principles thinking - asking fundamental questions to dissect and understand a problem which eventually leads to one-of-a-kind solutions, each as distinct as a fingerprint.  
  
Through NaN(O), a coding event driven by Sahaj across multiple colleges in India, they want to instil a culture of applying first principles thinking to a problem statement.  
  
------  
  

  
## Problem statement  
This is a **demo repository** for a test taker to get a feel of how the testing on the system works and how to submit a successful solution. The actual problem employees similar testing strategies.    

The problem statement is to create an actual calculator with a couple of endpoints. The structure of request response has been shared with the user.

------

#### API contract  
##### GET /caluclator/greeting
Checks whether the service is available.  
  
###### Response  
* Code: 200  
* Content: `Hello world!`  


##### POST /calculator/add  
Adds two given numbers
  
###### Request & Response headers  
Content-Type: application/json  
  
###### Body  
```  
{  
    first: number,
    second: number 
}  
```

###### Success Response  
* Status code: 200  
* Content: `{ result: result-of-the-summation }`  


##### POST /calculator/subtract

Subtracts two given numbers
  
###### Request & Response headers  
Content-Type: application/json  
  
###### Body  
```  
{  
    first: number,
    second: number
}  
```

###### Success Response  
* Status code: 200  
* Content: `{ result: result-of-the-subtraction }`  
  

###### How to submit a solution
In order to submit a solution, follow these steps.

- Fork the **nano-demo-calculator-app** repository ([How to fork a repository github](https://docs.github.com/en/get-started/quickstart/fork-a-repo))
    - Deselect the "Copy the main branch only" to copy other language demos as well
- Clone the forked repository ([How to clone a repository github](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository))
- Change the branch according to the language of your choice (This demo is available in (language-> branch) "kotlin"-> main, "node" -> "node", "python" -> "python", "cpp" -> "cpp" ) ([How to change branches git ](https://www.freecodecamp.org/news/git-switch-branch/))
- Enable workflows in your github fork (Under the actions tab -> Select "I understand my workflows, go ahead and enable them" to enable the test workflow)
- Use your favourite editor to make changes
- Create a commit after testing it locally ([How to commit git](https://github.com/git-guides/git-commit))
- Push the commit to the remote **to the same branch** (github repo) ([How to push git](https://docs.github.com/en/get-started/using-git/pushing-commits-to-a-remote-repository))
- If all your changes work well, you will see a green tick on the actions section on your repo under the selected branch ([How to see last run action](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/viewing-workflow-run-history))
  - If it's a cross mark, the logs will tell you what you did wrong.
  - Fix the issue, and repeat steps 4+ to resubmit
- Congratulations, you have successfully solved the dummy problem and are ready for the actual event.


###### Hint
An actual solution is present in one of the commits. If you revert the commit with the message "Remove actual answers", you should be able to get to a working solution
