import spacy

nlp = spacy.load("en_core_web_sm")

# Define keywords and phrases for each category
feature_keywords = ["add", "new", "feature", "functionality",
                    "enhancement", "improvement", "capability", "option"]
bug_keywords = ["fix", "error", "bug", "issue",
                "problem", "crash", "fault", "flaw"]
refactoring_keywords = ["refactor", "improve", "clean", "optimize",
                        "simplify", "streamline", "consolidate", "reorganize"]
documentation_keywords = ["document", "explain", "instruction",
                          "guide", "manual", "tutorial", "reference", "help"]
testing_keywords = ["test", "unit", "integration", "automated",
                    "manual", "coverage", "regression", "performance"]
deployment_keywords = ["deploy", "release", "ship",
                       "install", "configure", "setup", "package", "deliver"]
maintenance_keywords = ["maintain", "support", "upgrade",
                        "update", "monitor", "backup", "restore", "troubleshoot"]

# Define categories
categories = ["Feature requests or new feature", "Bug fixes",
              "Code Refactoring", "Documentation", "Testing", "Deployment", "Maintenance"]


def get_task_info(message):
    # Initialize counters for each category
    category_counts = {category: 0 for category in categories}

    # Analyze the message with spaCy
    doc = nlp(message.lower())

    # Check for keywords and phrases related to each category
    for token in doc:
        if any(keyword in token.text for keyword in feature_keywords):
            category_counts["Feature requests or new feature"] += 1
        if any(keyword in token.text for keyword in bug_keywords):
            category_counts["Bug fixes"] += 1
        if any(keyword in token.text for keyword in refactoring_keywords):
            category_counts["Code Refactoring"] += 1
        if any(keyword in token.text for keyword in documentation_keywords):
            category_counts["Documentation"] += 1
        if any(keyword in token.text for keyword in testing_keywords):
            category_counts["Testing"] += 1
        if any(keyword in token.text for keyword in deployment_keywords):
            category_counts["Deployment"] += 1
        if any(keyword in token.text for keyword in maintenance_keywords):
            category_counts["Maintenance"] += 1

    # Identify the category with the highest count
    max_count = max(category_counts.values())
    if max_count == 0:
        task_type = "Other"
    else:
        task_type = [category for category,
                     count in category_counts.items() if count == max_count][0]
        
    # Check if task has bug fixes or code refactors
    task_has_bug_fixes = "true" if category_counts["Bug fixes"] != 0 else "false"
    task_has_codes_refactors = "true" if category_counts["Code Refactoring"] != 0 else "false"

    return task_type, task_has_bug_fixes, task_has_codes_refactors


def get_has_bug_fixing(message, has_bugs):
    # Analyze the message with spaCy
    doc = nlp(message.lower())
    # Check for keywords and phrases related to each category
    for token in doc:
        if any(keyword in token.text for keyword in bug_keywords) or has_bugs:
            return True
        
    return False

def get_has_refactoring(message, has_refactor):
    # Analyze the message with spaCy
    doc = nlp(message.lower())
    # Check for keywords and phrases related to each category
    for token in doc:
        if any(keyword in token.text for keyword in refactoring_keywords) or has_refactor:
            return True
        
    return False
