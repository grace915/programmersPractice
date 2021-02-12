package Hash;

import java.util.Arrays;

public class Marathon {


    public String Matathon(String[] participant, String[] completion) {
        String answer = "";
        String temp = "";


        //오름차순으로 정리!
        Arrays.sort(participant);
        Arrays.sort(completion);
        int i = 0;
        while (i < completion.length) {
            if (!participant[i].equals(completion[i])) {
                temp = participant[i];
                break;
            } else {
                i++;
            }

        }
        if (!temp.equals("")) {
            answer = temp;
        } else {
            answer = participant[participant.length - 1];
        }
        return answer;
    }

}
