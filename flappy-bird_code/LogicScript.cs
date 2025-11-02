using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SocialPlatforms.Impl;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class LogicScript : MonoBehaviour
{
    public int PlayerScore;
    public int Highscore;
    public Text ScoreText;
    public Text HStext;
    public GameObject GameOverScreen;

    [ContextMenu ("increace score")]
    public void addscore(int scoretoadd)
    {
        PlayerScore = PlayerScore + scoretoadd;
        ScoreText.text = PlayerScore.ToString();
        Debug.Log("Score increaced");
    }


    public void GameRestart()
    {
        SceneManager.LoadScene(SceneManager.GetActiveScene().name);
    }

    public void GameOver()
    {
        GameOverScreen.SetActive(true); 
    }
}