package main

import (
	"fmt"
	"hash/fnv"
	"log"
	"math/rand"
	"os"
	"time"
)

var letterRunes = []rune("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

func RandStringRunes(n int) string {
	b := make([]rune, n)
	for i := range b {
		b[i] = letterRunes[rand.Intn(len(letterRunes))]
	}
	return string(b)
}

func CreateJobs(amount int) []string {
	var jobs []string

	for i := 0; i < amount; i++ {
		jobs = append(jobs, RandStringRunes(8))
	}
	return jobs
}

func DoWork(word string, id int) {
	h := fnv.New32a()
	h.Write([]byte(word))
	time.Sleep(time.Second)
	if os.Getenv("DEBUG") == "true " {
		fmt.Printf("Worker [%d] - created hash [%d] from word [%s]\n", id, h.Sum32(), word)
	}

}

type Work struct {
	ID  int
	Job string
}

type Worker struct {
	ID            int
	WorkerChannel chan chan Work
	Channel       chan Work
	End           chan bool
}

func (w *Worker) Start() {
	for {
		w.WorkerChannel <- w.Channel
		select {
		case job := <-w.Channel:
			DoWork(job.Job, w.ID)
		case <-w.End:
			return
		}
	}
}

func (w *Worker) Stop() {
	log.Printf("Worker [%d] is stopping", w.ID)
	w.End <- true
}

var WorkerChannel = make(chan chan Work)

type Collector struct {
	Work chan Work
	End  chan bool
}

func (c *Collector) Start(workers []Worker, input chan Work, end chan bool) {
	for {
		select {
		case <-end:
			for _, w := range workers {
				w.Stop()
			}
			return
		case work := <-input:
			worker := <-WorkerChannel
			worker <- work
		}
	}
}

func StartDispatcher(workerCount int) *Collector {
	var i int
	var workers []Worker
	input := make(chan Work)
	end := make(chan bool)

	collector := &Collector{Work: input, End: end}

	for i < workerCount {
		i++
		log.Println("starting worker:", i)
		worker := Worker{
			ID:            i,
			Channel:       make(chan Work),
			WorkerChannel: WorkerChannel,
			End:           make(chan bool)}
		go worker.Start()
		workers = append(workers, worker)
	}

	go collector.Start(workers, input, end)

	return collector
}

const WORKER_COUNT = 5
const JOB_COUNT = 100

func main() {
	log.Println("Starting app")
	c := StartDispatcher(WORKER_COUNT)

	for i, job := range CreateJobs(JOB_COUNT) {
		c.Work <- Work{
			Job: job,
			ID:  i,
		}
	}
}
