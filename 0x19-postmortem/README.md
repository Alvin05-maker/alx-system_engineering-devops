POSTMORTEM  FOR A PAYMENT PROCESSING SERVICE


Incident management

Issue Summary
Duration: August 19, 2024, 03:00 pm EAT  to August 19, 2024, 06:15 pm East African Time
Impact: The payment processing service was down for 3 hours and 15 minutes. Users experienced errors during checkout, leading to an inability to complete transactions. Approximately 70% of users attempting to make payments were inconvenienced.

Timelines
03:00 pm  - Issue detected: Automated monitoring systems flagged a significant increase in transaction failures.
03:05 pm - Detection method: Monitoring alert triggered my on-call dashboard, highlighting a surge in payment gateway errors.
03:15 pm - Initial investigation: I began investigating logs and identified unusual error rates from the payment gateway component.
03:45 pm - Misleading path: Initial suspicion pointed towards a possible database overload, leading to checks on database performance and connections, which were found to be normal.
04:15 pm - Escalation: Incident escalated to the infrastructure team for a deeper investigation into the payment gateway's integration with external services.
05:00 pm - Discovery: Found that the payment gateway API rate limit had been exceeded due to an unanticipated traffic surge.
06:00 pm - Resolution: Implemented a temporary increase in API rate limits and adjusted the load balancer configuration to handle higher traffic.
06:15 pm - Full restoration: Payment processing service was fully operational, and normal transaction flow resumed.

Root Cause and Resolution
Root Cause: The issue was caused by an API rate limit breach on the payment gateway due to an unanticipated surge in transaction volume. The payment gateway's API had a limit that was exceeded, resulting in failed transactions.
Resolution: The immediate fix involved temporarily increasing the API rate limits with the payment gateway provider and reconfiguring the load balancer to better distribute incoming traffic. Long-term, we worked with the payment gateway provider to implement a more scalable solution and improved rate limit thresholds.
Corrective and Preventative Measures

Improvements:
Enhance monitoring and alerting systems to better track API usage and thresholds in real-time.
Develop a more robust rate-limiting strategy with the payment gateway provider to handle traffic surges gracefully.
Implement a more scalable load balancing strategy to manage high transaction volumes.
Tasks:

Patch: Update the payment gateway integration to include more detailed API usage metrics.
Monitoring: Add comprehensive monitoring and alerting on API rate limits and transaction failure rates.
Configuration: Reconfigure load balancers to improve traffic distribution and implement auto-scaling policies.
Collaboration: Work with the payment gateway provider to review and optimize API rate limits and traffic handling.
Documentation: Update incident response playbooks to include steps for handling API rate limit breaches and high traffic volumes.

