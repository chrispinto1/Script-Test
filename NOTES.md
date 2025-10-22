# Just some notes put here, too long for a python docstring

# NOTES:

## possible apis available to read from:

### GET - https://stats-api.mlssoccer.com/matches/MLS-MAT-00067D/commentary? - 
#### Not sure if this would be for this use case as there's no images in the return and <s>also see that its paginated by 20 instances at a time and with a parameter of page_token which I won't know the value of</s>. Actually found that it's given in the pagination response as next_page_token

#### confirmed that the commentary without a next_page_token is the last one in the pagination and it's a missing key and not set to null

#### Commentary API setup:
    {
        commentary: Array<Event/Commentary>,
        match_info: Object - match data like date, name, season, etc
        next_page_token
    }

## XML format:
    <Event 
        MatchId="MLS-MAT-00067D" 
        EventTime="2025-10-19T00:27:29.765+02:00" 
        EventId="804100000214"
        Y-Source-Position="55.92" 
        X-Position="96.51" 
        Y-Position="55.92" 
        X-Source-Position="96.51">
        
        <Play 
            BallPossessionPhase="214" 
            PenaltyBox="false" 
            SemiField="false" 
            Evaluation="unsuccessful" 
            FlatCross="false" 
            Distance="medium" 
            Recipient="MLS-OBJ-0000EF" 
            Height="flat" 
            FromOpenPlay="true" 
            Player="MLS-OBJ-000398" 
            Team="MLS-CLU-000008">
            
            <Pass 
                FreeKickLayup="false"/>
            <Cross 
                GoalKeeperInterference="rebounded" 
                GoalKeeper="MLS-OBJ-000006" 
                Side="right"/>

        </Play>
        <OtherBallAction 
            BallPossessionPhase="215"
            Player="MLS-OBJ-0000EF"
            Team="MLS-CLU-000009"/>

        <ThrowIn 
            Side="left" 
            DecisionTimestamp="2025-10-19T00:27:07.212+02:00" 
            Team="MLS-CLU-000008">
            <Play>
                <Pass/>
            </Play>
        </ThrowIn>
        
        <Delete/>
        
        <KickOff 
            TeamLeft="MLS-CLU-000008"
            GameSection="firstHalf"
            TeamRight="MLS-CLU-000009">
        </KickOff>

        <TacklingGame 
            BallPossessionPhase="36" 
            Winner="MLS-OBJ-00089U" 
            WinnerTeam="MLS-CLU-000008" 
            GoalKeeperInvolved="false" 
            WinnerRole="withBallControl" 
            Loser="MLS-OBJ-0007XU" 
            LoserRole="withoutBallControl" 
            LoserTeam="MLS-CLU-000009" 
            DribbleEvaluation="successful" 
            Type="ground" 
            WinnerResult="dribbledAround"/>

        <GoalKick 
            DecisionTimestamp="2025-10-19T00:14:35.313+02:00"
            Team="MLS-CLU-000009">
            <Play>
                <Pass/>
            </Play>
        </GoalKick>

        <Foul 
            TeamFouled="MLS-CLU-000008" 
            Fouled="MLS-OBJ-000528" 
            TeamFouler="MLS-CLU-000009" 
            FoulType="foul" Fouler="MLS-OBJ-0007KK"/>

        <FreeKick 
            ExecutionMode="direct" 
            DecisionTimestamp="2025-10-19T00:16:32.001+02:00" 
            Team="MLS-CLU-000008">

            <Play>
                <Pass/>
            </Play>

        </FreeKick>

        <CornerKick 
            Rotation="towardsGoal" 
            PostMarking="none" 
            Side="right" 
            TargetArea="nearPost" 
            DecisionTimestamp="2025-10-19T00:17:32.000+02:00" 
            Placing="nearPost" Team="MLS-CLU-000009">

            <Play>
                <Pass/>
            </Play>

        </CornerKick>

        <ShotAtGoal 
            ChanceEvaluation="chance" 
            AfterFreeKick="false" 
            Player="MLS-OBJ-0000EB"
            ShotCondition="notComplicated"
            Team="MLS-CLU-000009"
            AssistAction="cornerKick"
            TypeOfShot="head" 
            PlayerSpeed="11.33" 
            ShotOrigin="3" 
            xG="0.2389" 
            BallPossessionPhase="108" 
            AngleToGoal="50.10" 
            SignificanceEvaluation="average" 
            Z-ShotTrace-Position="4.52" 
            CounterAttack="false" 
            AmountOfDefenders="4" 
            DistanceToGoal="5.62" 
            AssistShotAtGoal="MLS-OBJ-0007XU" 
            TakerSetup="cornerKick" 
            Y-ShotTrace-Position="30.50" 
            SetupOrigin="right" 
            AssistTypeShotAtGoal="direct" 
            TakerBallControl="volley" 
            BuildUp="cornerKick" 
            Pressure="3.15" 
            GoalDistanceGoalkeeper="0.70" 
            InsideBox="true">

                <ShotWide 
                    PitchMarking="over" 
                    Placing="far"/>

                <SavedShot 
                    SaveResult="held" 
                    GoalKeeper="MLS-OBJ-000006" 
                    SaveEvaluation="average" 
                    SaveType="arms"/>
                
                <SuccessfulShot 
                    AssistType="others" 
                    GoalZone="11" 
                    Solo="true" 
                    CurrentResult="0:1"
                    Assist="MLS-OBJ-000398"/>
                
                <ShotWoodWork Location="rightPost"/>
                
                <OtherShot/>
                
        </ShotAtGoal>

        <Caution 
            OtherReason="foul" 
            Reason="foul" 
            CardRating="yellow" 
            CardColor="yellow" 
            Player="MLS-OBJ-0007XP" 
            Team="MLS-CLU-000008"/>

        <OnFieldTreatment 
            EndEventTime="2025-10-19T00:36:55.323+02:00" 
            Duration="113" 
            Player="MLS-OBJ-0000E6" 
            Team="MLS-CLU-000009"/>

        <FinalWhistle 
            FinalResult="2:5" 
            BreakingOff="false" 
            GameSection="secondHalf"/>
        
        <GoalDisallowed 
            Reason="offside"
            Player="MLS-OBJ-0007XP"
            Team="MLS-CLU-000008"/>

        <SpectacularPlay 
            Type="backheel" 
            Player="MLS-OBJ-0000AF" 
            Team="MLS-CLU-000008"/>
        
        <Nutmeg 
            AffectedTeam="MLS-CLU-000009" 
            AffectedPlayer="MLS-OBJ-0007XU" 
            Player="MLS-OBJ-000398" 
            Team="MLS-CLU-000008"/>
        
        <RefereeBall/>
            
        <BallDeflection 
            Type="postRight" 
            Player="MLS-OBJ-000396" 
            Team="MLS-CLU-000008"/>

        <BallClaiming 
            BallPossessionPhase="161" 
            Type="BallHeld" 
            Player="MLS-OBJ-000006"
            Team="MLS-CLU-000008"/>
        
        <VarNotification 
            Status="complete" 
            Review="silentCheck" 
            Result="goal" 
            Decision="goal" 
            Reason="other" 
            EndEventTime="2025-10-19T00:55:32.342+02:00" 
            Incident="goal" 
            TestMode="false" 
            Team="MLS-CLU-000009"/>
        
        <Offside 
            Player="MLS-OBJ-0000EF"
            Team="MLS-CLU-000009"/>

        <AdditionalTimeDisplayed Minute="6"/>
        
        <Substitution 
            Infringement="none" 
            PlayerOut="MLS-OBJ-0007XQ" 
            Concussion="false" 
            PlayingPosition="IVR" 
            PlayerIn="MLS-OBJ-0007FB" 
            Team="MLS-CLU-000008"/>

        <BlockedShot 
            GoalPrevented="false" 
            Player="MLS-OBJ-0003DV"/>
        
        <FinalWhistle 
            FinalResult="2:5" 
            BreakingOff="false" 
            GameSection="secondHalf"/>
        
        <OtherPlayerAction 
            TreatmentRule="true" 
            PlayerOutofPitch="playerOffField" 
            PlayerBecomesGoalkeeper="false" 
            PlayerReturnTime="2025-10-19T00:24:45.820+02:00" 
            ChangeOfCaptain="false" 
            ChangeContingentExhausted="false" 
            Player="MLS-OBJ-0007XX" 
            Team="MLS-CLU-000008"/>

        <Penalty 
            GoalkeeperBehaviour="regular" 
            GoalkeeperMovement="left" 
            PlayersInBox="both" 
            CausingPlayer="MLS-OBJ-00006Q" 
            ProspectiveTaker="MLS-OBJ-000396" 
            RetakenPenalty="false" 
            DecisionTimestamp="2025-10-19T01:38:47.110+02:00" 
            Team="MLS-CLU-000008">

            <ShotAtGoal>
                <SuccessfulShot/>
            </ShotAtGoal>

        </Penalty>
            
    </Event>


    Actions are recorded into the Event tag
        - it can contain children of the following tags:
            1. Play - which can also have children of tags:
                a. Pass
                b. Cross
            2. OtherBallAction - no children
            3. ThrowIn - which can contain children of tags:
                a. Play
            4. Delete
            5. KickOff - which can contain children of tags:
                a. Play
            6. TacklingGame
            7. GoalKick - which can contain children of tags:
                a. Play
            8. Foul
            9. FreeKick - which can contain children of tags:
                a. Play
            10. CornerKick - which can contain children of tags:
                a. Play
            11. ShotAtGoal - which can contain children of tags:
                a. ShotWide
                b. SavedShot
                c. SuccessfulShot
                d. ShotWoodWork
                e. OtherShot
            12. Caution
            13. OnFieldTreatment
            14. GoalDisallowed
            15. SpectacularPlay
            16. Nutmeg
            17. RefereeBall
            18. BallDeflection
            19. BallClaiming
            20. VarNotification
            21. Offside
            22. AdditionalTimeDisplayed
            23. Substitution
            24. BlockedShot
            25. FinalWhistle
            26. OtherPlayerAction
            27. Penalty - which can contain children of tags:
                a. ShotAtGoal