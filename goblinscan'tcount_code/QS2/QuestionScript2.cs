using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class QuestionScript2 : MonoBehaviour
{
    private float randomnum1;
    private float randomnum2;
    public float Answer = 0;
    public float FA1 = 0;
    public float FA2 = 0;
    public float FA3 = 0;
    public Text questiontext;
    public Text AnswerText0;
    public Text AnswerText1;
    public Text AnswerText2;
    public Text AnswerText3;
    public Text ScoreText;
    public int Location;
    public int score;
    public int Health;
    public SavedData SD;
    public int Questionselect;
    public GameObject Goblin;
    public GameObject QuestionUI;
    public GameObject PauseMenu;

    // Start is called before the first frame update
    void Start()
    {
        score = SD.Score;
        ScoreText.text = score.ToString();
        Health = SD.Health;
        QuestionSelect();
    }

    //Activates the pause menu
    private void Update()
    {
        if(Input.GetKeyUp(KeyCode.Escape))
        {
            Goblin.SetActive(false);
            QuestionUI.SetActive(false);
            PauseMenu.SetActive(true);
        }
    }

    public void QuestionSelect()
    {
        Questionselect = Random.Range(0, 4);

        if (Questionselect == 0)
        {
            GenerateQ();
        }

        else if (Questionselect == 1)
        {
            GenerateQSubtract();
        }

        else if (Questionselect == 2)
        {
            GenerateQMultiply();
        }

        else if (Questionselect == 3)
        {
            GenerateQDivide();
        }
    }

    //generates an addition question
    [ContextMenu("generate addition Question")]
    public void GenerateQ()
    {
        //generates 2 random numbers and calculates the answer
        randomnum1 = Random.Range(1, 101);
        randomnum2 = Random.Range(1, 101);
        //Decides where the correct answer will be located
        Location = Random.Range(0, 2);
        //calculates the answer
        Answer = randomnum1 + randomnum2;
        //Activates the fake answer function
        FakeAnswer();
        //activates answerlocation function
        AnswerLocation();
        //turns a string in c# into text for the unity editor to display within the UI
        questiontext.text = string.Format("What is {0} + {1}?", randomnum1, randomnum2);
        //Saves the score variable
        PlayerPrefs.SetInt("Score", score);

    }

    [ContextMenu("generate subtraction Question")]
    public void GenerateQSubtract()
    {
        //generates 2 random numbers and calculates the answer
        randomnum1 = Random.Range(1, 101);
        randomnum2 = Random.Range(1, 101);
        //Decides where the correct answer will be located
        Location = Random.Range(0, 2);
        //calculates the answer
        Answer = randomnum1 - randomnum2;
        //Activates the fake answer function
        FakeAnswer();
        //activates answerlocation function
        AnswerLocation();
        //turns a string in c# into text for the unity editor to display within the UI
        questiontext.text = string.Format("What is {0} - {1}?", randomnum1, randomnum2);
        //Saves the score variable
        PlayerPrefs.SetInt("Score", score);

    }

    //generates a multiplication question
    [ContextMenu("generate multiplication Question")]
    public void GenerateQMultiply()
    {
        //generates 2 random numbers and calculates the answer
        randomnum1 = Random.Range(1, 101);
        randomnum2 = Random.Range(1, 101);
        //Decides where the correct answer will be located
        Location = Random.Range(0, 2);
        //calculates the answer
        Answer = randomnum1 * randomnum2;
        //Activates the fake answer function
        FakeAnswer();
        //activates answerlocation function
        AnswerLocation();
        //turns a string in c# into text for the unity editor to display within the UI
        questiontext.text = string.Format("What is {0} * {1}?", randomnum1, randomnum2);
        //Saves the score variable
        PlayerPrefs.SetInt("Score", score);

    }

    //generates a division question
    [ContextMenu("generate division Question")]
    public void GenerateQDivide()
    {
        //generates 2 random numbers and calculates the answer
        randomnum1 = Random.Range(1, 101);
        randomnum2 = Random.Range(1, 101);
        //Decides where the correct answer will be located
        Location = Random.Range(0, 2);
        //calculates the answer
        Answer = randomnum1 / randomnum2;
        //Activates the fake answer function
        FakeAnswer();
        //activates answerlocation function
        AnswerLocation();
        //turns a string in c# into text for the unity editor to display within the UI
        questiontext.text = string.Format("What is {0} / {1}?", randomnum1, randomnum2);
        //Saves the score variable
        PlayerPrefs.SetInt("Score", score);

    }

    //Adds to the score and checks if score is over 10 it changes to the next level of questions
    public void Score()
    {
        score = score + 1;
        ScoreText.text = score.ToString();
        SD.UpdateData2();
    }

    //checks player's health and determines if it should trigger game over or remove a life
    public void Fail()
    {
        if (Health != 0)
        {
            Health = Health - 1;
            SceneManager.LoadScene(1);
        }

        else
        {
            SceneManager.LoadScene(2);
        }
    }

    //Selects the location of the correct and incorrect answer
    public void AnswerLocation()
    {
        if (Location == 0)
        {
            Debug.Log("correct answer top left");
            AnswerText0.text = Answer.ToString();
            AnswerText1.text = FA1.ToString();
            AnswerText2.text = FA2.ToString();
            AnswerText3.text = FA3.ToString();
        }

        if (Location == 1)
        {
            Debug.Log("correct answer top right");
            AnswerText0.text = FA1.ToString();
            AnswerText1.text = Answer.ToString();
            AnswerText2.text = FA2.ToString();
            AnswerText3.text = FA3.ToString();
        }

        if (Location == 2)
        {
            Debug.Log("correct answer bottom left");
            AnswerText0.text = FA2.ToString();
            AnswerText1.text = FA1.ToString();
            AnswerText2.text = Answer.ToString();
            AnswerText3.text = FA3.ToString();
        }

        if (Location == 3)
        {
            Debug.Log("correct answer bottom right");
            AnswerText0.text = FA3.ToString();
            AnswerText1.text = FA1.ToString();
            AnswerText2.text = FA2.ToString();
            AnswerText3.text = Answer.ToString();
        }


    }

    //creates a fake answer and checks to see if it matches the correct answer. If it does, Fake answer is regenerated until they dont match
    public void FakeAnswer()
    {
        FA1 = Answer + Random.Range(-5, 5);
        FA2 = Answer + Random.Range(-5, 5);
        FA3 = Answer + Random.Range(-5, 5);

        while (FA1 == Answer)
        {
            FA1 = Answer + Random.Range(-5, 5);
        }

        while (FA2 == Answer || FA2 == FA1)
        {
            FA2 = Answer + Random.Range(-5, 5);
        }

        while (FA3 == Answer || FA3 == FA1 || FA3 == FA2)
        {
            FA3 = Answer + Random.Range(-5, 5);
        }
    }

}
