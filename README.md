1. ### Project Setup
| Syntax | Description |
| ----------- | ----------- |
| `DOCKER_BUILDKIT=1 docker build . --progress=plain `  |Build using docker |
| `DOCKER_BUILDKIT=1 docker-compose build --progress=plain `  |Build using docker-compose |
| `docker-compose run --rm app sh -c "python manage.py makemigrations"`  | make migrations|

| `docker-compose run --rm app sh -c "python manage.py migrate"`  | migrate |
| `docker-compose run --rm app sh -c "python manage.py test"`  | Ensure all tests are running |
| `docker-compose up`  | Start the project |
| `docker-compose down`  | Stop the project |
| `docker-compose run --rm app sh -c "django-admin startapp core"`  | Start app |

| `docker-compose run --rm app sh -c "django-admin startproject app ."`  | Start project in the current directory |
| `docker-compose run --rm app sh -c "django-admin startapp core"`  | Start app |

### **Onboarding App**
- Used for creating, updating and viewing onboardings.

**Onboarding App structure**
- app/onboarding/tests/
- app/onboarding/urls
- app/onboarding/serializers
- app/onboarding/apps
- app/onboarding/views

### **Policies App**
- Used for creating, updating and viewing policies.

**Policy App structure**
- app/policies/tests/
- app/policies/urls
- app/policies/serializers
- app/policies/apps
- app/policies/views


### **Knowledge Base App**
- Used organizational information, including policies, compliance guidelines, and onboarding materials.

**Knowledge Basestructure**
- app/knowledgebase/tests/
- app/knowledgebase/urls
- app/knowledgebase/serializers
- app/knowledgebase/apps
- app/knowledgebase/views
