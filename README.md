# AFPGDIP2022
Letterkenny Institute of Technology - Postgraduate Diploma in DevOps 2021-2022  
DevOps Project Management  
Addams Family Accommodation Team Assignment  


## Table of Contents

[Table of Contents](#table-of-contents)  
[Preamble](#preamble)  
[Product Owner](#product-owner)  
[Rockstars](#team-members)
[Project Deadline](#project-deadline)  
[Project Specification](#project-specification)  
[Considerations](#considerations)  
[Useful Links](#useful-links)  
[Risk Register](#risk-register)  
[Tenants of Design](#tenants-of-design)  
[Social Contract](#social-contract)  

## Preamble

This is the online repository for the Addams Family Accommodation Project.

- The end customer would like an online booking system for a range of hotels and holiday homes. 
- Their most popular product is Haunted Houses. 
- The system must take details from a customer and map them to the room/suites/houses available along with a single box for extra ‘nice to have’ requests. 
- The system should be clean and simple. 
- Your team has been tasked with creating the pipeline for the SDLC. 
- You have also been asked to provide a simple prototype page(s) to test the pipeline. 
- The system needs to take into account the usual security requirements. 
- The administrator of the end system (Adams family member) should be able to access detailed information and edit as appropriate. 
- Once the client enters details it should not be able to be changed by the holiday maker.

Our product will be delivered using an Agile methodology that embraces the DevOps culture. Please note that our culture embraces change and these documents are treated as living, breathing artefacts that will be continuously updated.

### Scrum Master
Rotates Weekly
- Sprint 1, Week 1 : Jeff Aitken
- Sprint 1, Week 2 : Lydia Shadwell
- Sprint 1, Week 3 : Ciarán Ó hÓgáin
- Sprint 2, Week 1 : James Bowman  
- Sprint 2, Week 2 : Kay O'Callaghan
- Sprint 2, Week 3 : Kieran Kelleher (Current)

### Product Owner
Rotates Weekly - The previous Scrum Master takes over as Product Manager

### Team Members
- Jeffrey Aitken
- James Bowman
- John Finegan
- Luis Uriel Cabrera Gonzalez
- Kieran Kelleher
- Kay O'Callaghan
- Ciarán Ó hÓgáin
- Lydia Shadwell

Lecturer: Paul Greaney


### Project Deadline
Friday April 1st - 23:59

## Project Specification  
<!-- <Our team agreed specifications are as follows>     -->
    - A clean and simple website design.
    - Two user access levels - Customer and Administrator.

    - Azure DevOps will be used to implement the pipeline.
    - The site will use the Python Flask Framework.
    - The site will be hosted on an Azure Virtual Machine with a MySQL Database.  

    - Azure Application Insights will be used for performance testing.
    - Azure DevOps will be used for source control management.
    - Azure DevOps be used for ticketing and sprint planning.
    - Azure DevOps Artifacts will be used as binary repository.
    - Postman / Newman will be used to perform unit testing.
    - Sphinx will be used for Automatic Documentation.  
    - SonarCloud will be used for security and code quality testing.
    

##Useful Links

[Project Slack Channel](https://app.slack.com/client/T84LE6L6R/C02P6U2S7RV)  
[Azure DevOps Ticketing](https://dev.azure.com/AddamsFamily/AddamsFamily2022/_backlogs/backlog/AddamsFamily2022%20Team/Stories/?showParents=true)   
[Azure Git Repository](https://dev.azure.com/AddamsFamily/AddamsFamily2022/_git/AddamsFamily2022?version=GBmain)  
[Azure DevOps Sprint Retrospectives](https://dev.azure.com/AddamsFamily/AddamsFamily2022/_apps/hub/ms-devlabs.team-retrospectives.home)  
Project close out presentation: TBC  
[Azure Readme Markdown Guide](https://docs.microsoft.com/en-us/azure/devops/project/wiki/markdown-guidance?view=azure-devops) 

## Risk Register

TO BE UPDATED - These are the current Risks on the project, re-aligned on a weekly basis

    1. Infrastructure proving to be a real problem, may block being able to release software
    2. Team is finding itself to be running short on time due to other work and study commitments
    3. No PO feedback on software
    4. Unknown technology choices has led to a lot of upskilling required
    5. Changing / ambiguous requirements
    6. Talk of the company being bought out has raised concerns
    7. Lack of rights for toolsets chosen has hindered progress and ability to deliver

## Tenants of Design
TO BE COMPLETED 
<pick from the sample sections below and add your own>  
1. Dedication to clean, secure, performant and self documented code  
    - code Frameworks used  
    - code coverage tool used  
    - Secure code: Regex for cleansing and validation, Named queries and database triggers  
    - performance testing tool to be used  
2. Documentation / code commenting (javadoc)/separate branch  
3. Datastore for persistance  
4. Testing: 
    - Unit testing  
    - integretation testing  
    - UA  
5. Environments:  
    - staging and production  
    - tight configuration management for consistency and reproducibility  
    - automated creation and deployments  
    - integrated and automated pipeline (commit -> test -> deploy)  
6. Github version control:  
    - branches used  
    - version/release management  
7. Agile project management methods/principles (jira)  

## Social Contract

### Meetings

    Stand-ups will occur on Tuesdays at 20:00 and Thursday at 18:45.  
    People give their updates in alphabetical order of those present at the meeting.  
    Updates will be in the form: What I've done, What I plan to do, Impediments.  
    Sprint planning will occur every Tuesday following the Stand-Up.  
    Please add and update items within Jira prior to the sprint planning session.  
    Sprint retro will occur on the first Thursday after a sprint concludes.  
    The order that people present their sprint retro updates will also be based on alphabetical order.  
    Points raised in standups and sprint retrospectives will be noted and posted on Slack channel by the Scrum Master.  
    Sprint retrospectives will also be captured in Azure DevOps. 
    
    Task estimation will be done using <<what method>>.  
    
    Come prepared to meetings.  
    Be on time for Stand Ups and meetings.  
    Mobile phones on silent.  
    Everyone has equal voice and valuable contribution.  
    Keep your language and tone professional at all times.  
    Be honest. 
 
### Communication

    Slack is the preferred method of communication.
    If a demonstration is required use Microsoft Teams (Record if possible).
    No Slack communications between 23:00 and 08:00.
    Raise a problem as soon as you see it.
    Respect each other and understand differences in knowledge.
    All team documents are to be created using Markdown language and shared on Git.
    There are no silly questions, if you don’t understand, ask.
    Share success stories.
    Focus on the positives.
    Don’t make assumptions.
    Don’t interrupt and cut another person off while they are talking.
    Listen when someone is talking, don’t interject.
    Zero tolerance for bullying.
    Communication in this order: Slack, EMail
    Agile way of working.
    If are assigned a job, take ownership of it and keep it up to date.
    Stick to your agreed working patterns. Let the team know when you are late or leaving early.
    Keep JIRA board updated at all times.
    Update the Scrum Board as you progress the story i.e. don’t update at standup.
    Don't be afraid to ask for help.
    Don't be afraid to give constructive critism, as long as it is constructive.
    Solve roadblocks within the team. 
    If the impediment can’t be solved within the team then give it to the Scrum Master.

## Other

    Sprints will start on January 11th with each sprint lasting three weeks.
    The Scrum Master role rotates each week, the schedule is available on the on the process section.
    The Product Owner role rotates each week, the schedule is available on the on the process section.
    Azure DevOps will be used for task management and planning.
    Each member of the team will work at least one story task per week, unless they need to take leave.

### Branching Strategy

TO BE COMPLETED

### Estimating Story Points Within Azure DevOps

The teams team's velocity is calculated by dividing the the number of points burned each sprint divided by no of sprints. The Velocity chart from Jira (below) is used for this calculation.

The teams current story point velocity is "<Choose the number!>".
