# Tech spike - Hosting

In this tech spike we compared GitLab Pages and DigitalOcean 
to decide which one to use to host our website.

## GitLab Pages 

### Pros
+ Very easy to setup and integrate with your GitLab project. 
+ Changes to the website are automatically deployed when you push your changes. 
+ It is free to use. 

### Cons
+ Does not support dynamic server-side processing.


## DigitalOcean

### Pros
+ Supports dynamic server-side processing. 
+ Would allow our tests to be faster and not limited. 
+ Would serve as a learning oppurtunity, for example webservers, CD, and Linux. 

### Cons
+ Is not free to use. (Note: With GitHub Student Pack you have access to a $50 voucher.)



## Verdict
We went with GitLab Pages because it's easy-to-use nature was a perfect fit for the current stage in our project.

# Tech spike - Js Vs TypeScript

In this tech spike we compared vanilla js and typescript.

## Vanilla Js

### Pros
+ We already know it/Easy to learn.
+ Our project is using vanilla js.
+ Does not require compilation.

### Cons
+ Not type safe.
+ Easy to miss bugs.

## TypeScript

### Pros
+ Is type safe.
+ Used in a lot of workspaces.
+ Early spotted bugs.
+ Readability.

### Cons
+ Requires compilation
+ Can be over complicated.
+ False sense of security.

## Verdict
We will change from vanilla js to typescript on a branch to test it out. If the tests shows good results we will switch it over on our master branch.