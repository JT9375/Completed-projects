using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class AnswerScript23 : MonoBehaviour
{
    public QuestionScript2 Qscript;



    private void OnCollisionEnter2D(Collision2D collision)
    {

        // checks for a collision and ensures the location of the answer matches with this collision to increace the score
        if (collision.gameObject.layer == 6 && Qscript.Location == 3)
        {
            Qscript.Score();
            Debug.Log("Score Increaced");
            Qscript.QuestionSelect();
        }

        // The collision doesn't mach the correct answer and activates the fail function
        else if(collision.gameObject.layer == 6 && Qscript.Location != 3)
        {
            Qscript.Fail();
        }


    }
}
