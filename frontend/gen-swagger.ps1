swagger-codegen generate -i ../backend/schema.yml -l javascript --additional-properties modelPropertyNaming=snake_case usePromises=true -o ./src/Api
