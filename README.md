# AFPGDIP2022
Letterkenny Institute of Technology - Postgraduate Diploma in DevOps 2021-2022  
DevOps Project Management  
Addams Family Accommodation Team Assignment  


## Table of Contents

       Table of Contents
        Preamble
            Product Owner
            Rockstars
        Project Deadline
        Project Specification
        Considerations
[Useful Links](#Useful-Links)
            For more information visit our other sections
        Risk Register
        Tenants of Design
        Social Contract

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
- Sprint 2, Week 1 : James Bowman (current)

### Product Owner
Rotates Weekly

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
    A clean and simple website design.
    Two user access levels - Customer and Administrator.

    Azure DevOps will be used to implement the pipeline.
    The site will use the Python Flask Framework.
    The site will be hosted on an Azure Virtual Machine with a MySQL Database.  

    Azure Application Insights will be used for performance testing.
    Azure DevOps will be used for source control management.
    Azure DevOps be used for ticketing and sprint planning.
    Azure DevOps Artifacts will be used as binary repository.
    Postman / Newman will be used to perform unit testing.
    Sphinx will be used for Automatic Documentation.  
    SonarCloud will be used for security and code quality testing.
    

##Useful Links

[Project Slack Channel](https://app.slack.com/client/T84LE6L6R/C02P6U2S7RV)  
[Azure DevOps Ticketing](https://dev.azure.com/AddamsFamily/AddamsFamily2022/_backlogs/backlog/AddamsFamily2022%20Team/Stories/?showParents=true)   
[Azure Git Repository](https://dev.azure.com/AddamsFamily/AddamsFamily2022/_git/AddamsFamily2022?version=GBmain)  
Project close out presentation: TBC  
[Azure Readme Markdown Guide](https://docs.microsoft.com/en-us/azure/devops/project/wiki/markdown-guidance?view=azure-devops) 

### More Information
For more information visit our other sections
Section     Description
Process     Describes the companies process
Project Log     Log of project activities
Costings    Overview of the project cost
Architecture    Outlines the architecture
Environments    Overview of the environment set-up
DR Plan     Disaster Recovery Plan and procedures
Requirements    Overview of the requirements for the project
SLAs    Service level agreements
Risk Management     How we manage risk
Security    Overview of security
Project Log     Team log for the project

## Risk Register

These are the current Risks on the project, re-aligned on a weekly basis

    Infrastructure proving to be a real problem, may block being able to release software
    Team is finding itself to be running short on time due to other work and study commitments
    No PO feedback on software
    Unknown technology choices has led to a lot of upskilling required
    Changing / ambiguous requirements
    Talk of the company being bought out has raised concerns
    Lack of rights for toolsets chosen has hindered progress and ability to deliver

## Tenants of Design
<pick from the sample sections below and add your own>
    Dedication to clean, secure, performant and self documented code
        code Frameworks used
        code coverage tool used
        Secure code: Regex for cleansing and validation, Named queries and database triggers
        performance testing tool to be used
    Documentation / code commenting (javadoc)/separate branch
    Datastore for persistance
    Testing:
        Unit testing
        integretation testing
        UA
    Environments:
        staging and production
        tight configuration management for consistency and reproducibility
        automated creation and deployments
        integrated and automated pipeline (commit -> test -> deploy)
    Github version control:
        branches used
        version/release management
    Agile project management methods/principles (jira)

## Social Contract

### Meetings

    Stand-ups will occur on Tuesdays at 20:00 and Thursday at 18:45.
    The order that people give their updates will be based on alphabetical order of those present at the meeting.
    Updates will be in the form: What I've done, What I plan to do, Impediments
    Sprint planning will occur every Tuesday following the Stand-Up.
    Please add and update items within Jira prior to the sprint planning session.
    Sprint retro will occur on the first Thursday after a sprint concludes.
    The order that people present their sprint retro updates will be based on alphabetical order of those present at the meeting.
    Points raised in standups and during the sprint retrospectives will be noted and posted on the slack channel by the Scrum Master.
    Sprint retrospectives will also be captured in Azure DevOps (https://dev.azure.com/AddamsFamily/AddamsFamily2022/_apps/hub/ms-devlabs.team-retrospectives.home)
    
    Task estimation will be done using <<what method>>.
    
    Come prepared to meetings.
    Be on time for Stand Ups and meetings.
    Mobile phones on silent.
    Everyone has equal voice and valuable contribution.
    Keep your language and tone professional at all times.
    Be honest.

### Communication

    Slack is the preferred method of communication.
    If a demonstration is required use Microsoft Teams.  If possible record the session and upload to the Slack channel.
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
    Communication in this order: Slace, EMail
    Agile way of working.
    If are assigned a job, take ownership of it and keep it up to date.
    Stick to your agreed working patterns. Let the team know when you are late or going early.
    Keep JIRA board updated at all times.
    Update the Scrum Board as you progress the story i.e. don’t update at standup.
    Don't be afraid to ask for help.
    Don't be afraid to give constructive critism, as long as it is constructive.
    Solve roadblocks within the team. If the impediment can’t be solved within the team then give it to the Scrum Master.

## Other

    Sprints will start on January 11th with each sprint lasting three weeks.
    The Scrum Master role rotates each week, the schedule is available on the on the process section
    The Product Owner role rotates each week, the schedule is available on the on the process section
    Azure DevOps will be used for task management and planning.
    Each member of the team will work at least one story task per week, unless they need to take leave.

### Branching Strategy


### Estimating Story Points Within Azure DevOps

The teams team's velocity is calculated by dividing the the number of points burned each sprint divided by no of sprints. The Velocity chart from Jira (below) is used for this calculation.

The teams current story point velocity is "<Choose the number!>".
