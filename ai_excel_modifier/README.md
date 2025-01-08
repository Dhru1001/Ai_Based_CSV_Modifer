**AI Excel Modifier**
=====================

**Description**
---------------

AI Excel Modifier is a web application that enables users to upload Excel or CSV files and perform various operations such as removing duplicates, applying filters, modifying rows, and more. It also provides options to download the modified file and logs of operations performed.

This application is designed to simplify data preprocessing tasks for non-technical users while leveraging powerful libraries like **Pandas** for data manipulation.

**Features**
------------

*   Upload and process Excel (.xlsx) and CSV (.csv) files.
    
*   Remove duplicate rows.
    
*   Apply custom filters and rules to the data.
    
*   Add or delete rows.
    
*   Download the modified file.
    
*   Download operation logs specific to the current user's actions.
    

**Installation and Setup**
--------------------------

### **1\. Clone the Repository**

First, clone the repository to your local machine using the following command:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`bashCopy codegit clone` 

### **2\. Navigate to the Project Folder**

Change the working directory to the project folder:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`bashCopy codecd` 

### **3\. Create and Activate a Virtual Environment (Optional)**

To isolate dependencies, it’s recommended to use a virtual environment:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   bashCopy code# Create virtual environment  python -m venv venv  # Activate the virtual environment  # On Windows:  venv\Scripts\activate  # On macOS/Linux:  source venv/bin/activate   `

### **4\. Install Dependencies**

Install the required Python libraries:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   bashCopy codepip install -r requirements.txt   `

### **5\. Set Up the Environment Variables**

Create a .env file in the project directory to store sensitive configuration variables. Example:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   plaintextCopy codeSECRET_KEY=your_secret_key_here   `

### **6\. Run the Application**

Navigate to the app directory and run the application using the following command:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   bashCopy codepython app.py   `

**Usage**
---------

1.  Open your web browser and navigate to http://localhost:5000.
    
2.  Upload an Excel or CSV file using the provided interface.
    
3.  Choose an operation to modify the file:
    
    *   Remove Duplicates
        
    *   Apply Filters
        
    *   Add or Delete Rows
        
4.  Download the modified file or the log of operations.
    

**Folder Structure**
--------------------

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   plaintextCopy codeproject-folder/  ├── app.py                # Main Flask application  ├── utils.py              # Utility functions for data manipulation  ├── templates/            # HTML templates  │   ├── index.html        # Home page template  │   ├── modify.html       # Modify page template  ├── static/               # Static files (CSS, JS, etc.)  ├── data/                 # Folder to store uploaded and temporary files  ├── logs/                 # Folder to store operation logs  ├── .env                  # Environment variables file  ├── requirements.txt      # List of required Python libraries  └── README.md             # Documentation file   `

**Features in Detail**
----------------------

### **1\. Remove Duplicates**

Automatically detect and remove duplicate rows in the uploaded file. Duplicates are handled case-insensitively.

### **2\. Apply Filters**

Apply custom filtering rules to narrow down or modify data.

### **3\. Add or Delete Rows**

Easily add new rows or delete specific rows by specifying conditions.

### **4\. Download Modified File**

After modifying the file, download the updated file in .csv format.

### **5\. Operation Logs**

The application logs all operations performed on the data and allows users to download these logs. Logs are specific to the current session, ensuring user privacy.

**Troubleshooting**
-------------------

### **Common Issues**

1.  **File Not Found Error:**Ensure the uploaded file exists in the data/ directory.
    
2.  **Environment Variables Error:**Make sure you have a .env file with the correct SECRET\_KEY.
    
3.  bashCopy codepip install -r requirements.txt
    

**License**
-----------

This project is licensed under the MIT License. Feel free to modify and distribute this project under the terms of the license.

**Contributing**
----------------

Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure that your code adheres to the existing style and includes appropriate comments/documentation.
