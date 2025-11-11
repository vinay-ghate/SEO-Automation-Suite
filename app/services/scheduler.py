from typing import Dict
from datetime import datetime

class SchedulerService:
    def __init__(self):
        self.schedules = {}
    
    def create_schedule(
        self,
        project_id: str,
        task_type: str,
        cron_expression: str
    ) -> Dict:
        schedule_id = f"schedule_{len(self.schedules) + 1}"
        
        schedule = {
            'schedule_id': schedule_id,
            'project_id': project_id,
            'task_type': task_type,
            'cron_expression': cron_expression,
            'enabled': True,
            'created_at': datetime.utcnow().isoformat()
        }
        
        self.schedules[schedule_id] = schedule
        return schedule
    
    def get_schedules(self, project_id: str) -> list:
        return [
            s for s in self.schedules.values()
            if s['project_id'] == project_id
        ]
    
    def update_schedule(self, schedule_id: str, enabled: bool) -> Dict:
        if schedule_id in self.schedules:
            self.schedules[schedule_id]['enabled'] = enabled
            return self.schedules[schedule_id]
        return None
    
    def delete_schedule(self, schedule_id: str) -> bool:
        if schedule_id in self.schedules:
            del self.schedules[schedule_id]
            return True
        return False
