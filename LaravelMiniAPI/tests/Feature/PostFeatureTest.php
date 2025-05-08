<?php

namespace Tests\Feature;

use App\Models\User;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Illuminate\Foundation\Testing\WithFaker;
use Tests\TestCase;

class PostFeatureTest extends TestCase
{
    /**
     * A basic feature test example.
     */
    public function test_authenticated_user_can_create_post()
    {
        $user = User::factory()->create();
        $response = $this->actingAs($user, 'sanctum')->postJson('/api/posts', [
            'content' => 'Hello world',
            'platform' => 'twitter',
        ]);
        $response->assertStatus(201);
    }

    public function test_guest_cannot_create_post()
    {
        $response = $this->postJson('/api/posts', [
            'content' => 'Hello world',
            'platform' => 'twitter',
        ]);
        $response->assertStatus(401);
    }

}
