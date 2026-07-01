
class Job_Application:
    def __init__(self, job_id, company_name, job_title, url, status, date_applied, last_updated):
        self.job_id = job_id
        self.company_name = company_name
        self.job_title = job_title
        self.url = url
        self.status = status
        self.date_applied = date_applied
        self.last_updated = last_updated
 
    def to_dict(self):
        return {
            "job_id": self.job_id,
            "company_name": self.company_name,
            "job_title": self.job_title,
            "url": self.url,
            "status": self.status,
            "date_applied": self.date_applied,
            "last_updated": self.last_updated
        }
 
    @staticmethod
    def from_dict(data):
        return Job_Application(
            data["job_id"],
            data["company_name"],
            data["job_title"],
            data["url"],
            data["status"],
            data["date_applied"],
            data["last_updated"]
        )
 



    