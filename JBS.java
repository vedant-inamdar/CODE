import java.util.*;

public class JBS{
    public static void main(String[] args) {
        int[][] jobs = { { 2, 30 }, { 1, 30 }, { 1, 70 }, { 2, 90 }, { 3, 30 } };
        jobScheduling(jobs);
    }

    public static void jobScheduling(int[][] jobs){
        int n=jobs.length;
        int[][] sortedJobs=new int[n][3];
        for(int i=0;i<n;i++){
            sortedJobs[i][0]=i;
            sortedJobs[i][1]=jobs[i][0];
            sortedJobs[i][2]=jobs[i][1];
        }
        Arrays.sort(sortedJobs,Comparator.comparingInt(job->job[2]));
        ArrayList<Integer>schedule=new ArrayList<>();
        int profit=0;
        boolean[] slot=new boolean[n];

        for(int i=n-1;i>=0;i--){
            int deadline=sortedJobs[i][1];
            int index=findSlot(slot,deadline);

            if(index!=-1){
                slot[index]=true;
                schedule.add(sortedJobs[i][0]);
                profit+=sortedJobs[i][2];
            }
        }
        System.out.println("Scheduled jobs:");
        
        for(int jobId:schedule){
            System.out.println("Job"+jobId);
        }
        System.out.println("Total profit:"+profit);
    }
    
    public static int findSlot(boolean[] slot,int deadline){
        for(int i=deadline-1;i>=0;i--){
            if(!slot[i]){
                return i;
            }
        }
        return -1;
    }
}