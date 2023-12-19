import { createQueue } from "kue";

const queue = createQueue();

const job = queue.create('push_notification_code', {
    phoneNumber: '08122420302',
    message: "is this a goodBye",
})

job.on('enqueue', () => {
    console.log(`Notification job created: ${job.id}`);
})

job.on('completed', () => {
    console.log('Notification job completed');
})

job.on('failed attempt', () => {
    console.log('Notification job failed');
})

job.save()
