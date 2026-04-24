db.createCollection("nonfiction" , {
    validator: {
        $jsonSchema: {
            required: ["name", "price"],
            properties: {
                name: {
                    bsonType: "string",
                    description: "Title of the book must be a string and is required"
                }, 
                price: {
                    bsonType: "number",
                    description: "Price of the book must be a number and is required"
                }
            }
        }
    },
    validationAction: "error"
})  

// Update the collection to include the authors field with the specified validation rules
db.runCommand({
    collMod: "nonfiction",
    validator: {
        $jsonSchema: {
            required: ["name", "price", "authors"],
            properties: {
                name: {
                    bsonType: "string",
                    description: "Title of the book must be a string and is required"
                }, 
                price: {
                    bsonType: "number",
                    description: "Price of the book must be a number and is required"
                },
            authors: {
                bsonType: "array",
                description: "Authors of the book must be an array and is required",
                items: {
                    bsonType: "object",
                    required: ["name", "email"],
                    properties: {
                        name: {
                            bsonType: "string"
                        },
                        email: {
                            bsonType: "string",
                            pattern: "^.+@.+$"
                        }
                    }}
                }
            }
        }
    },
    validationAction: "error"
})  



