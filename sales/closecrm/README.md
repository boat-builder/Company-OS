# Close CRM CLI

A command-line interface for interacting with Close CRM.

## Setup

### 1. Install Dependencies

```bash
pip install click requests
```

### 2. Configure API Key

Create a `.env` file in the same directory as `close_cli.py`:

```
CLOSE_API_KEY=api_xxxxxxxxxxxxx
```

You can find your API key in Close: **Settings > API Keys**

## Usage

```bash
python close_cli.py [COMMAND] [SUBCOMMAND] [OPTIONS]
```

### Get Help

```bash
python close_cli.py --help
python close_cli.py lead --help
python close_cli.py lead create --help
```

---

## Commands

### Lead Management

```bash
# Create a lead
python close_cli.py lead create -n "Acme Corp" -u "https://acme.com" -d "Enterprise prospect"

# List leads (with optional filters)
python close_cli.py lead list
python close_cli.py lead list -l 25 --status-id stat_xxx --sort -date_updated

# Search leads
python close_cli.py lead search -q "acme"
python close_cli.py lead search -n "Acme" --status-id stat_xxx

# Get lead details (includes contacts)
python close_cli.py lead get lead_xxx

# Update a lead
python close_cli.py lead update lead_xxx -n "Acme Corp Inc" --status-id stat_yyy

# Delete a lead
python close_cli.py lead delete lead_xxx
python close_cli.py lead delete lead_xxx --yes   # skip confirmation
```

### Contact Management

```bash
# Add a contact to a lead (emails, phones, urls are repeatable)
python close_cli.py contact create lead_xxx -n "Jane Doe" -t "CEO" -e "jane@acme.com" -p "+1-555-1234" -u "https://linkedin.com/in/janedoe"

# Add multiple emails
python close_cli.py contact create lead_xxx -n "Bob" -e "bob@acme.com" -e "bob@gmail.com"

# List contacts for a lead
python close_cli.py contact list lead_xxx

# Get contact details
python close_cli.py contact get cont_xxx

# Update a contact
python close_cli.py contact update cont_xxx -n "Jane Smith" -t "CTO"

# Delete a contact
python close_cli.py contact delete cont_xxx
```

### Task Management

```bash
# Create a task (due date defaults to tomorrow)
python close_cli.py task create -l lead_xxx -t "Follow up on proposal"
python close_cli.py task create -l lead_xxx -t "Send contract" -d 2026-03-15

# List tasks
python close_cli.py task list
python close_cli.py task list --pending --show-lead
python close_cli.py task list -l lead_xxx

# Update a task
python close_cli.py task update task_xxx --text "Updated description" --due-date 2026-03-20

# Complete a task
python close_cli.py task complete task_xxx

# Delete a task
python close_cli.py task delete task_xxx
```

### Notes

```bash
# Add a note to a lead
python close_cli.py note create lead_xxx -t "Had a great intro call, interested in our platform"

# List notes for a lead
python close_cli.py note list lead_xxx
python close_cli.py note list lead_xxx -l 20
```

### Utilities

```bash
# List all lead statuses (with IDs for filtering)
python close_cli.py status list

# Show current authenticated user
python close_cli.py whoami
```

---

## Example Workflows

### Onboard a new lead with contacts

```bash
python close_cli.py lead create -n "New Corp" -u "https://newcorp.com"
# Copy the lead_xxx ID from output

python close_cli.py contact create lead_xxx -n "Alice Lee" -t "VP Marketing" -e "alice@newcorp.com"
python close_cli.py contact create lead_xxx -n "Bob Chen" -t "CTO" -e "bob@newcorp.com"
python close_cli.py task create -l lead_xxx -t "Schedule intro call"
python close_cli.py note create lead_xxx -t "Referred by existing customer"
```

### Find and follow up on a lead

```bash
python close_cli.py lead search -n "Acme"
python close_cli.py lead get lead_xxx
python close_cli.py contact list lead_xxx
python close_cli.py task create -l lead_xxx -t "Send proposal" -d 2026-03-20
python close_cli.py note create lead_xxx -t "Discussed pricing, following up with proposal"
```

---

## Extending the CLI

The CLI is built with [Click](https://click.palletsprojects.com/) and designed to be easily extensible. All API methods live in the `CloseAPI` class, and CLI commands use Click's group/command decorators with context passing.

### Adding API Methods

```python
class CloseAPI:
    def my_method(self, param: str) -> dict:
        return self.get(f"/endpoint/{param}/")
```

### Adding CLI Commands

```python
@lead.command("mycommand")
@click.argument("lead_id")
@click.pass_context
def lead_mycommand(ctx, lead_id: str):
    """Description."""
    api: CloseAPI = ctx.obj["api"]
    result = api.my_method(lead_id)
    click.echo(click.style("Done!", fg="green"))
```

---

## Close API Reference

- [Close API Documentation](https://developer.close.com/)
- [Lead Endpoints](https://developer.close.com/resources/leads)
- [Contact Endpoints](https://developer.close.com/resources/contacts)
- [Task Endpoints](https://developer.close.com/resources/tasks)
- [Activity Endpoints](https://developer.close.com/resources/activities)

---

## Troubleshooting

### "CLOSE_API_KEY not found in .env file"

Make sure your `.env` file is in the same directory as `close_cli.py` and contains `CLOSE_API_KEY=your_key` (no quotes around the key).

### "API Error (401): Unauthorized"

Your API key may be invalid or expired. Generate a new one in Close: **Settings > API Keys**

### "API Error (404): Not Found"

The resource ID doesn't exist. Use `lead list`, `contact list`, or `task list` to find valid IDs.
