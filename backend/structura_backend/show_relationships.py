from app.models import FieldWorker, Supervisors, Project

print('\n=== SHOWING PROJECT-BASED RELATIONSHIPS ===\n')

# Get the supervisor
supervisor = Supervisors.objects.get(email='crunch.super@structura.com')
print(f'Supervisor: {supervisor.first_name} {supervisor.last_name}')
print(f'Email: {supervisor.email}')
print(f'Assigned to project_id: {supervisor.project_id.project_id if supervisor.project_id else "None"}')
print(f'Project name: {supervisor.project_id.project_name if supervisor.project_id else "None"}')
print()

# Get workers for this supervisor's project
if supervisor.project_id:
    workers_for_supervisor = FieldWorker.objects.filter(project_id=supervisor.project_id)
    print(f'Field workers on project {supervisor.project_id.project_id}: {workers_for_supervisor.count()} workers')
    if workers_for_supervisor.exists():
        for w in workers_for_supervisor:
            print(f'  ✓ {w.first_name} {w.last_name} ({w.role}) - ₱{w.payrate}/day')
    else:
        print('  ❌ NO WORKERS FOUND FOR THIS PROJECT')
else:
    print('❌ Supervisor has no project assigned')

print()
print('=' * 60)
print('ALL FIELD WORKERS BY PROJECT:')
print('=' * 60)

for project in Project.objects.all().order_by('project_id'):
    worker_count = FieldWorker.objects.filter(project_id=project).count()
    if worker_count > 0:
        print(f'\n📁 Project {project.project_id}: {project.project_name}')
        print(f'   Workers: {worker_count}')
        workers = FieldWorker.objects.filter(project_id=project)
        for w in workers:
            print(f'   - {w.first_name} {w.last_name} ({w.role})')
