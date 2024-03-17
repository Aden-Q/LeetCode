class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        mod = 10 ** 9 + 7

        @cache
        def dp(total_to_play, songs_played) -> int:            
            if songs_played > n:
                return 0

            if total_to_play == 0:
                return 1 if songs_played == n else 0

            # in the current state, we play a song, this song can either be:
            # 1. the song we played before, possible if songs_played >= k + 1
            # 2. a new song that we haven't played before
            # we have (n - songs_played) new songs for option 1
            num_playlists = (n - songs_played) * dp(total_to_play-1, songs_played+1)
            if songs_played >= k + 1:
                # we have songs_played choices to repeat for option 2
                num_playlists += (songs_played - k) * dp(total_to_play-1, songs_played)

            return num_playlists % mod

        # we want to listen to goal songs, and every songs must be played at least once
        return dp(goal, 0)
