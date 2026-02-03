from app.models import FieldWorker, Supervisors, Project

print('\n=== FIXING FIELD WORKERS ===\n')

# Get the supervisor's project
supervisor = Supervisors.objects.get(email='crunch.super@structura.com')
target_project = supervisor.project_id

print(f'Supervisor: {supervisor.first_name} {supervisor.last_name}')
print(f'Target project_id: {target_project.project_id} ({target_project.project_name})')
print()

# Get all field workers currently on project 18
old_project = Project.objects.get(project_id=18)
workers = FieldWorker.objects.filter(project_id=old_project)

print(f'Found {workers.count()} workers on project 18 ({old_project.project_name})')
print(f'Reassigning them to project 25 ({target_project.project_name})...\n')

# Update all workers to the supervisor's project
updated_count = 0
for worker in workers:
    print(f'  ✓ {worker.first_name} {worker.last_name} ({worker.role})')
    worker.project_id = target_project
    worker.save()
    updated_count += 1

print(f'\n✅ Successfully reassigned {updated_count} workers to project {target_project.project_id}')
print('\nVerifying...')

# Verify the change
workers_on_25 = FieldWorker.objects.filter(project_id=target_project)
print(f'Workers now on project 25: {workers_on_25.count()}')
for w in workers_on_25:
    print(f'  - {w.first_name} {w.last_name} ({w.role})')

print('\n✅ DONE! Field workers will now show up in the supervisor dashboard.')
