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

### 3. Make it Executable (Optional)

```bash
chmod +x close_cli.py
```

## Usage

```bash
python close_cli.py [COMMAND] [SUBCOMMAND] [OPTIONS]
```

### Get Help

```bash
# General help
python close_cli.py --help

# Help for a specific command group
python close_cli.py task --help
python close_cli.py lead --help

# Help for a specific subcommand
python close_cli.py task create --help
```

## Commands

### Task Management

#### Create a Task

```bash
python close_cli.py task create --lead-id <LEAD_ID> --text "Task description"
```

**Options:**
| Option | Short | Required | Description |
|--------|-------|----------|-------------|
| `--lead-id` | `-l` | Yes | Lead ID (e.g., `lead_xxx`) |
| `--text` | `-t` | Yes | Task description |
| `--due-date` | `-d` | No | Due date (YYYY-MM-DD), defaults to tomorrow |
| `--assigned-to` | `-a` | No | User ID to assign task to |

**Examples:**

```bash
# Create a task due tomorrow (default)
python close_cli.py task create -l lead_abc123 -t "Follow up on proposal"

# Create a task with specific due date
python close_cli.py task create -l lead_abc123 -t "Send contract" -d 2026-01-20

# Assign task to specific user
python close_cli.py task create -l lead_abc123 -t "Call client" -a user_xyz789
```

#### List Tasks

```bash
python close_cli.py task list
```

**Options:**
| Option | Short | Description |
|--------|-------|-------------|
| `--lead-id` | `-l` | Filter tasks by lead ID |

**Examples:**

```bash
# List all tasks
python close_cli.py task list

# List tasks for a specific lead
python close_cli.py task list -l lead_abc123
```

---

### Lead Management

#### List Leads

```bash
python close_cli.py lead list
```

**Options:**
| Option | Short | Default | Description |
|--------|-------|---------|-------------|
| `--limit` | `-n` | 10 | Maximum number of leads to return |

**Examples:**

```bash
# List first 10 leads
python close_cli.py lead list

# List first 25 leads
python close_cli.py lead list -n 25
```

#### Search Leads

```bash
python close_cli.py lead search --query "search term"
```

**Options:**
| Option | Short | Description |
|--------|-------|-------------|
| `--query` | `-q` | Raw search query (supports Close search syntax) |
| `--name` | `-n` | Search by exact lead name |
| `--limit` | `-l` | Maximum number of results (default: 10) |

**Examples:**

```bash
# Search by keyword
python close_cli.py lead search -q "influx"

# Search with Close query syntax
python close_cli.py lead search -q "status:Potential"

# Limit results
python close_cli.py lead search -q "marketing" -l 5
```

#### Get Lead Details

```bash
python close_cli.py lead get <LEAD_ID>
```

**Example:**

```bash
python close_cli.py lead get lead_abc123
```

---

### Lead Statuses

#### List All Statuses

```bash
python close_cli.py status list
```

This shows all available lead statuses with their IDs, useful for filtering or creating leads.

---

### Utility Commands

#### Show Current User

```bash
python close_cli.py whoami
```

Displays the authenticated user's name, email, and user ID.

---

## Extending the CLI

The CLI is built with [Click](https://click.palletsprojects.com/) and designed to be easily extensible.

### Adding a New Command Group

```python
@cli.group()
def mygroup():
    """Description of your command group."""
    pass

@mygroup.command("subcommand")
@click.option("--option", "-o", help="Option description")
@click.pass_context
def mygroup_subcommand(ctx, option):
    """Description of subcommand."""
    api: CloseAPI = ctx.obj["api"]
    # Your implementation here
```

### Adding API Methods

Add new methods to the `CloseAPI` class:

```python
class CloseAPI:
    # ... existing methods ...

    def my_new_method(self, param: str) -> dict:
        """Description of what this does."""
        return self.get(f"/endpoint/{param}/")
```

### Common Patterns

**Making a GET request:**
```python
result = api.get("/endpoint/", params={"key": "value"})
```

**Making a POST request:**
```python
result = api.post("/endpoint/", json={"key": "value"})
```

**Displaying colored output:**
```python
click.echo(click.style("Success!", fg="green"))
click.echo(click.style("Warning!", fg="yellow"))
click.echo(click.style("Error!", fg="red"))
```

**Handling errors:**
```python
raise click.ClickException("Something went wrong")
raise click.UsageError("Invalid option combination")
```

---

## Close API Reference

- [Close API Documentation](https://developer.close.com/)
- [Lead Endpoints](https://developer.close.com/resources/leads)
- [Task Endpoints](https://developer.close.com/resources/tasks)
- [Search Query Syntax](https://developer.close.com/topics/searching)

---

## Examples Workflow

### Quick follow-up workflow

```bash
# 1. Search for a lead
python close_cli.py lead search -q "acme"

# 2. Get lead details (copy the lead ID from search results)
python close_cli.py lead get lead_abc123

# 3. Create a follow-up task
python close_cli.py task create -l lead_abc123 -t "Send pricing proposal" -d 2026-01-15

# 4. Verify task was created
python close_cli.py task list -l lead_abc123
```

---

## Troubleshooting

### "CLOSE_API_KEY not found in .env file"

Make sure your `.env` file:
- Is in the same directory as `close_cli.py`
- Contains `CLOSE_API_KEY=your_key` (no quotes around the key)

### "API Error (401): Unauthorized"

Your API key may be invalid or expired. Generate a new one in Close: **Settings > API Keys**

### "API Error (404): Not Found"

The resource ID (lead_id, task_id, etc.) doesn't exist. Double-check the ID.
