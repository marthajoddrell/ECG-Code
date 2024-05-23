#!/bin/bash -l
# Use the current working directory
#SBATCH -D ./

# Use the current environment for this job
#SBATCH --export=All

# Define job name
#SBATCH  -J mae_init

# Define a standard output file. When the job is running, %N will be replaced by the name of
# the first node where the job runs, %j will be replaced by job id number.
#SBATCH -o slurm.%N.%j.out

# Define a standard error file
#SBATCH -e slurm.%N.%j.err

# Request the GPU partition (gpulowsmall, or gpudacdt/gputroisi if you have dedicated access). We don't recommend requesting multiple partitions, as the specifications of the nodes in these partitions are different.
#SBATCH -p gpu

# Request the number of nodes
#SBATCH -N 1

# Request the number of GPUs per node to be used (if more than 1 GPU per node is required, change 1 into Ngpu, where Ngpu=2)
#SBATCH --gres=gpu:1



# Request the number of CPU cores. (There are 48 CPU cores and 2 GPUs on each GPU node in partition gpulowsmall/gpudacdt/gputroisi,
# so please request 24*Ngpu CPU cores, i.e., 24 CPU cores for 1 GPU, 48 CPU cores for 2 GPUs).
# SBATCH -n 1

#SBATCH --ntasks-per-node=2    # total number of tasks per node
#SBATCH --cpus-per-task=24

# Set time limit in format a-bb:cc:dd, where a is days, b is hours, c is minutes, and d is seconds.
# SBATCH -t 5-00:00:00

# Request the memory on the node or request memory per core
# PLEASE don't set the memory option as we should use the default memory which is based on the number of cores
# SBATCH --mem=90GB or #SBATCH --mem-per-cpu=9000M

# Insert your own username to get e-mail notifications (note: keep just one "#" before SBATCH)
##SBATCH --mail-user=

# Notify user by email when certain event types occur
#SBATCH --mail-type=ALL
#s
# Set your maximum stack size to unlimited
ulimit -s unlimited

# export MASTER_PORT=$(expr 10000 + $(echo -n $SLURM_JOBID | tail -c 4) + $SLURM_ARRAY_TASK_ID)
# Load tensorflow and relevant modules
module purge
# module load apps/anaconda3/5.2.0
module remove libs/cudnn/7.6.3_cuda10.0.130
module remove libs/cuda/10.0.130
module load libs/cudnn/8.2.1_cuda11.3
module load libs/cuda/11.3
module load compilers/gcc/5.5.0
module load mpi/openmpi/1.10.7/gcc-5.5.0

module load/apps/anaconda3/2023.03-poetry
source activate openmmlab1


module list

echo =========================================================
echo "mpiexec=`which mpiexec`"
echo "mpirun=`which mpirun`"
echo SLURM job: submitted  date = `date`
date_start=`date +%s`

# echo Executable file:                              
# echo MPI parallel job.                                  
# echo -------------  
# echo Job output begins                                           
# echo -----------------                                           
# echo
echo "CUDA_VISIBLE_DEVICES : $CUDA_VISIBLE_DEVICES"
echo "GPU_DEVICE_ORDINAL   : $GPU_DEVICE_ORDINAL"
hostname
echo Current directory: `pwd`
echo "Print the following environmetal variables:"
echo "Job name                     : $SLURM_JOB_NAME"
echo "Job ID                       : $SLURM_JOB_ID"
echo "Job user                     : $SLURM_JOB_USER"
echo "Job array index              : $SLURM_ARRAY_TASK_ID"
echo "Submit directory             : $SLURM_SUBMIT_DIR"
echo "Temporary directory          : $TMPDIR"
echo "Submit host                  : $SLURM_SUBMIT_HOST"
echo "Queue/Partition name         : $SLURM_JOB_PARTITION"
echo "Node list                    : $SLURM_JOB_NODELIST"
echo "Hostname of 1st node         : $HOSTNAME"
echo "Number of nodes allocated    : $SLURM_JOB_NUM_NODES or $SLURM_NNODES"
echo "Number of processes          : $SLURM_NTASKS"
echo "Number of processes per node : $SLURM_TASKS_PER_NODE"
echo "Requested tasks per node     : $SLURM_NTASKS_PER_NODE"
echo "Requested CPUs per task      : $SLURM_CPUS_PER_TASK"
echo "Scheduling priority          : $SLURM_PRIO_PROCESS"
echo "OMP_NUM_THREADS              : $SLURM_CPUS_ON_NODE"
echo "OMPI_COMM_WORLD_SIZE         : $OMPI_COMM_WORLD_SIZE"
echo "OMPI_COMM_WORLD_RANK         : $OMPI_COMM_WORLD_RANK"
echo "SLURM_NTASKS                 : $SLURM_NTASKS"
echo "proc_id                      : $SLURM_PROCID"
echo "node_list                    : $SLURM_NODELIST"

echo "Running parallel job:"

CONFIG_FILE='/sharedscratch/MAEscripts/mae_vit-base-p16_8xb512-amp-coslr-300e_in1k.py'

export NCCL_P2P_LEVEL=NVL


srun python /sharedscratch/mmpretrain/tools/train.py $CONFIG_FILE --launcher slurm


#conda deactivate

date_end=`date +%s`
seconds=$((date_end-date_start))
minutes=$((seconds/60))
seconds=$((seconds-60*minutes))
hours=$((minutes/60))
minutes=$((minutes-60*hours))
echo =========================================================
echo SLURM job: finished   date = `date`
echo Total run time : $hours Hours $minutes Minutes $seconds Seconds
echo =========================================================
