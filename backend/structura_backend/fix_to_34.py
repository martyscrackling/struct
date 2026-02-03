from app.models import FieldWorker, Project

print('\n=== REASSIGNING WORKERS TO PROJECT 34 ===\n')

# Get project 34
target_project = Project.objects.get(project_id=34)
print(f'Target project: {target_project.project_id} - {target_project.project_name}')
print()

# Get all field workers currently on project 25
workers = FieldWorker.objects.filter(project_id__project_id=25)

print(f'Found {workers.count()} workers on project 25')
print(f'Moving them to project 34...\n')

# Update all workers to project 34
updated_count = 0
for worker in workers:
    print(f'  ✓ {worker.first_name} {worker.last_name} ({worker.role})')
    worker.project_id = target_project
    worker.save()
    updated_count += 1

print(f'\n✅ Successfully reassigned {updated_count} workers to project 34')

# Verify
workers_on_34 = FieldWorker.objects.filter(project_id=target_project)
print(f'\nWorkers now on project 34: {workers_on_34.count()}')
for w in workers_on_34:
    print(f'  - {w.first_name} {w.last_name} ({w.role})')

print('\n✅ DONE!')
