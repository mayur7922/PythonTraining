import json

def validate_schema(entry, required_fields):
    missing_fields = [field for field in required_fields if field not in entry]
    return missing_fields

def generate_summary_report(json_file, required_fields):
    try:
        with open(json_file, 'r') as file:
            data = json.load(file)
        
        total_entries = len(data)
        missing_field_counts = {field: 0 for field in required_fields}
        entries_with_issues = 0
        
        for entry in data:
            missing_fields = validate_schema(entry, required_fields)
            if missing_fields:
                entries_with_issues += 1
                for field in missing_fields:
                    missing_field_counts[field] += 1
        
        report = {
            "total_entries": total_entries,
            "entries_with_issues": entries_with_issues,
            "missing_field_counts": missing_field_counts
        }
        
        return report
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


required_fields = ["id", "name", "email"]
summary_report = generate_summary_report('data.json', required_fields)


if summary_report:
    print("Summary Report:")
    print(f"Total Entries: {summary_report['total_entries']}")
    print(f"Entries with Issues: {summary_report['entries_with_issues']}")
    print("Missing Field Counts:")
    for field, count in summary_report['missing_field_counts'].items():
        print(f"  {field}: {count}")
